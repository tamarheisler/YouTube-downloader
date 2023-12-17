from flask import Flask, render_template, request, jsonify
from downloader import downloadVideo,downloadPlaylist

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    choice = request.form['choice']
    url = request.form['url']
    download_format = request.form['format']
    try:
        if "youtube" in url:
            if choice == '1':
                downloadVideo(url, download_format)
            elif choice == '2':
                downloadPlaylist(url, download_format)
            elif choice == '3':
                # downloadChannel(url, download_format)
                downloadPlaylist(url, download_format)
        return jsonify({"status": "success", "message": "Finished successfully"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
