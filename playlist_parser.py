import re
from pytube import Playlist, YouTube 

def get_playlist(playlist_url):
    playlist = None
    if verify_url(playlist_url):
        print(f"Playlist URL: {playlist_url}")
        playlist = Playlist(playlist_url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    else:
        print(f"Invalid playlist URL: {playlist_url}")
    return playlist

def get_videos(playlist):
    videos = []
    if playlist:
        print('Number of videos in playlist: %s' % len(playlist.video_urls))
        for video in playlist.videos:
            videos.append(video)
    else:
        print("Invalid playlist")    
    return videos

def get_video_streams(videos):
    video_streams = []
    print("Process videos streams")
    for video in videos:
        try:
            print(f": {video.title}")
            video_data = {
                'title': video.title,
                'stream': video.streams.get_highest_resolution()
            }
            video_streams.append(video_data)
        except Exception as err:
            print(f"Exception occured {err}")
    return video_streams


def verify_url(playlist_url):
    if not playlist_url: 
        return False
    else:
        pattern = re.compile(r'https://www\.youtube\.(?:com|de|fr|...)/(?:playlist|watch)\?list=.+')
        return bool(re.match(pattern, playlist_url))
