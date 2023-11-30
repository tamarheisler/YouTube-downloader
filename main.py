
from flask import Flask, render_template, request
from pytube import YouTube, Playlist, Channel
from vimeo_downloader import Vimeo

app = Flask(__name__)

def downloadSingle(parsedUrl, format):
    if format == 'mp4':
        parsedUrl.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    elif format == 'mp3':
        parsedUrl.streams.filter(only_audio=True).first().download(filename=f"{parsedUrl.title}.mp3")
    elif format == 'avi':
        parsedUrl.streams.filter(only_audio=True).first().download(filename=f"{parsedUrl.title}.avi")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    choice = request.form['choice']
    url = request.form['url']
    download_format = request.form['format']

    if "youtube" in url:
        if choice == '1':
            yt = YouTube(url)
            downloadSingle(yt, download_format)
        elif choice == '2':
            playlist = Playlist(url)
            print('Number of videos in playlist: %s' % len(playlist.video_urls))
            for video in playlist.videos:
                print('downloading : {} with url : {}'.format(video.title, video.watch_url))
                video.streams.\
                    filter(type='video', progressive=True, file_extension='mp4').\
                    order_by('resolution').desc().first().download()
        elif choice == '3':
            c = Channel(url)
            # print(f'Downloading videos by {c.channel_name}')
            for video in c.videos:
                print('downloading : {} with url : {}'.format(video.title, video.watch_url))
                video.streams.first().download()
    elif "vimeo" in url:
        if choice == '1':
            v = Vimeo(url)
            if download_format == 'mp4':
                v.streams[-1].download(filename=f"{v.metadata.title}.mp4")
            elif download_format == 'mp3':
                v.streams[-1].download(filename=f"{v.metadata.title}.mp3")
            elif download_format == 'avi':
                v.streams[-1].download(filename=f"{v.metadata.title}.avi")
    return "Finished successfully"


if __name__ == '__main__':
     app.run(debug=True)




