import re
from pytube import Playlist, YouTube 

def get_playlist(playlist_url):
    playlist = None
    try:
        print(f"Playlist URL: {playlist_url}")
        playlist = Playlist(playlist_url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    except Exception as err:
        print(f"Invalid playlist URL: {err}")
    return playlist

def get_videos(playlist):
    videos = []
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    if playlist:
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