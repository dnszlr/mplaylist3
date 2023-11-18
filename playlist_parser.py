import re
from pytube import Playlist, YouTube 

limit = 100

def get_playlist(playlist_url):
    print(f"Playlist URL: {playlist_url}")
    videos = []
    playlist = Playlist(playlist_url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    return playlist

def get_videos(playlist):
    videos = []
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    if playlist:
        video_amount = len(playlist.video_urls)
        if video_amount <= limit:
            for video in playlist.videos:
                videos.append(video)
        else:
            print(f"Can't download {playlist.title} because it contains more than {limit} videos")    
    else:
        print("Invalid playlist URL")    
    return videos

def get_video_streams(videos):
    video_streams = []
    print("Process videos streams")
    for video in videos:
        print(f": {video.title}")
        video_data = {
            'title': video.title,
            'stream': video.streams.get_highest_resolution()
        }
        video_streams.append(video_data)
    return video_streams