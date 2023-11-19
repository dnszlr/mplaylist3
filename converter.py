from moviepy.editor import AudioFileClip
from file_handling import get_out_folder
import os, logging

def convert_to_mp3(data, playlist_title):
    output_folder = get_out_folder()
    os.makedirs(output_folder, exist_ok=True)
    playlist_folder = os.path.join(output_folder, playlist_title)
    os.makedirs(playlist_folder, exist_ok=True)
    try:
        # Download as mp4
        title = replace_forbidden_characters(data['title'] + ".mp4")
        title = filter_non_ascii(title);
        print(f"Downloading Title: {title}")
        data['stream'].download(filename = title, output_path = playlist_folder)
        mp4 = os.path.join(playlist_folder, title)
        logging.debug(f"MP4 is: {mp4}")
        mp3 = os.path.join(playlist_folder, title[:-1] + '3')
        logging.debug(f"MP3 is: {mp3}")
        # Convert to mp3
        audio_clip = AudioFileClip(mp4)
        audio_clip.write_audiofile(mp3)
        audio_clip.close()
        os.remove(mp4)
    except Exception as err:
        logging.debug(f"Inner error while downloading or converting {data['title']} to mp3 with {err}")

def replace_forbidden_characters(title):
    forbidden_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in forbidden_characters:
        title = title.replace(char, '_')
    return title

def filter_non_ascii(title):
    return title.encode('ascii', 'ignore').decode('ascii')