#
# from flask import Flask, render_template, request
# from pytube import YouTube, Playlist, Channel
# #from vimeo_downloader import Vimeo
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/download', methods=['POST'])
# def download():
#     choice = request.form['choice']
#     url = request.form['url']
#     download_format = request.form['format']
#     #download_location = request.form['location']
#     if choice == '1':
#         yt = YouTube(url)
#         print(f'Downloading videos by {url.title()}')
#         if download_format == 'mp4':
#             yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
#         elif download_format == 'mp3':
#             yt.streams.filter(only_audio=True).first().download(filename=f"{yt.title}.mp3")
#         elif download_format == 'avi':
#             yt.streams.filter(only_audio=True).first().download(filename=f"{yt.title}.avi")
#     elif choice == '2':
#         p = Playlist(url)
#         print(f'Downloading videos by {p.title}')
#         for video in p.videos:
#             video.streams.first().download()
#     elif choice == '3':
#         c = Channel(url)
#         print(f'Downloading videos by {c.channel_name}')
#         for video in c.videos:
#             video.streams.first().download()
#     return "Finished successfully"
#
#
# if __name__ == '__main__':
#      app.run(debug=True)

from flask import Flask, render_template, request
from pytube import YouTube, Playlist, Channel
import os

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    choice = request.form['choice']
    url = request.form['url']
    download_format = request.form['format']

    # Get the selected directory
    download_location = request.files['location']

    # Ensure the directory exists
    if not os.path.exists(download_location):
        return "Invalid download location"

    if choice == '1':
        yt = YouTube(url)
        print(f'Downloading videos by {yt.title}')
        if download_format == 'mp4':
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(
                output_path=download_location)
        elif download_format == 'mp3':
            yt.streams.filter(only_audio=True).first().download(output_path=download_location,
                                                                filename=f"{yt.title}.mp3")
        elif download_format == 'avi':
            yt.streams.filter(only_audio=True).first().download(output_path=download_location,
                                                                filename=f"{yt.title}.avi")
    elif choice == '2':
        p = Playlist(url)
        print(f'Downloading videos from {p.title}')
        for video in p.videos:
            video.streams.first().download(output_path=download_location)
    elif choice == '3':
        c = Channel(url)
        print(f'Downloading videos from {c.channel_name}')
        for video in c.videos:
            video.streams.first().download(output_path=download_location)

    return "Finished successfully"


if __name__ == '__main__':
    app.run(debug=True)
