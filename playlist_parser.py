from pytube import Playlist 
import re
import logger as Logger

from classes import Video

def get_playlist(playlist_url):
    Logger.info(f"Starting preview of playlist with url: {playlist_url}")
    playlist = None
    if verify_url(playlist_url):
        try:
            playlist = Playlist(playlist_url)
            playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        except Exception as err:
            Logger.error(f"Couldn't read playlist url, check internet connection {err}")
    else:
        Logger.debug(f"The passed url {playlist_url} is not a playlist")
    return playlist

def get_videos(playlist):
    videos = []
    if playlist:
        Logger.info(f"Amount of videos in playlist: {len(playlist.video_urls)}")
        for video in playlist.videos:
            videos.append(video)
    else:
        Logger.debug("Invalid playlist")
    return videos

def get_streams(videos):
    video_streams = []
    Logger.info("Process videos streams")
    for video in videos:
        try:
            Logger.info(f"Receiving stream for {video.title}")
            video_data = Video(video.title, video.streams.get_highest_resolution())
            video_streams.append(video_data)
        except Exception as err:
            Logger.debug(f"Exception occured while getting video streams: {err}")
    return video_streams


def verify_url(playlist_url):
    if not playlist_url: 
        return False
    else:
        pattern = re.compile(r'https://www\.youtube\.(?:com|de|fr|...)/(?:playlist|watch)\?list=.+')
        return bool(re.match(pattern, playlist_url))
