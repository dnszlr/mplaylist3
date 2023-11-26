from pytube import Playlist, YouTube
import re
import logger as Logger

from classes import Wrapper, Video

video_pattern = re.compile(r'^https://www\.youtube\.(?:com|de|fr|...)/watch\?v=.+')
playlist_pattern = re.compile(r'https://www\.youtube\.(?:com|de|fr|...)/playlist\?list=.+')

def get_playlist_from_url(url):
    Logger.info(f"Receiving song information for {url}")
    playlist = None
    try:
        if verify_url(url, video_pattern):
            video = YouTube(url)
            playlist = Wrapper(video.title, [video])
        elif verify_url(url,playlist_pattern):    
            playlist = Playlist(url)
            playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
            videos = get_videos_from_playlist(playlist)
            playlist = Wrapper(playlist.title, videos)
        else:
            Logger.debug(f"The passed url {url} is not a video or playlist")
    except Exception as err:
        Logger.error(f"Couldn't read url, {err}")
    return playlist

def get_videos_from_playlist(playlist):
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


def verify_url(url, pattern):
    if not url: 
        return False
    else:
        return bool(re.match(pattern, url))