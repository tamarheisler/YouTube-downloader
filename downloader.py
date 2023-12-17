import os
from pytube import Playlist, YouTube
from pytube.exceptions import VideoUnavailable

LOCATION = "downloads"

def response(success, message, data):
    return {
        "success": success,
        "message": message,
        "data": data
    }

def get_video_metadata(location, video):
    return {
        "title": video.title,
        "image": video.thumbnail_url,
        "author": video.author,
        "location": location
    }

def save_video(video, extension):
    base, _ = os.path.splitext(os.path.basename(video))
    new_file = os.path.join(os.path.dirname(video), f"{base}.{extension}")
    os.rename(video, new_file)
    return new_file

def downloadSingle(*, location, pytube_instance, extension):
    try:
        video = pytube_instance.streams.filter().get_highest_resolution().download(location)
        new_file = save_video(video, extension)
        metadata = get_video_metadata(new_file, pytube_instance)
        print(metadata)
        return response(True, "video downloaded successfully", [metadata])
    except VideoUnavailable:
        return response(False, f"{pytube_instance.title} not available", None)

def downloadVideo(url: str, extension: str):
    youtube = YouTube(url)
    location = f"{LOCATION}/"
    return downloadSingle(
        location=location,
        pytube_instance=youtube,
        extension=extension
    )

def downloadPlaylist(url: str, extension: str):
    playlist = Playlist(url=url)
    location = f"{LOCATION}/{extension}/{playlist.title}/"
    metadata = []
    for video in playlist.videos:
        metadata = downloadSingle(
            location=location,
            pytube_instance=video,
            extension=extension
        )
    return {"success": True, "message": "playlist downloaded successfully"}

# Example usage:
# downloadVideo("https://www.youtube.com/watch?v=VIDEO_ID", "mp4")
# downloadPlaylist("https://www.youtube.com/playlist?list=PLAYLIST_ID", "mp4")
