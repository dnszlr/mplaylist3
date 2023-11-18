import sys
from converter import convert_to_mp3
from playlist_parser import get_playlist, get_videos, get_video_streams

def main():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <playlist_url>")
        sys.exit(1)
    
    playlist_url = sys.argv[1]
    playlist = get_playlist(str(playlist_url))
    playlist_title = playlist.title
    videos = get_videos(playlist)
    streams = get_video_streams(videos)
    convert_to_mp3(streams, playlist_title)

if __name__ == "__main__":
    main()

