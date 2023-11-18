import os
from datetime import datetime
from moviepy.editor import AudioFileClip

def convert_to_mp3(data, playlist_title):
    output_folder = os.path.join("./out", playlist_title)
    os.makedirs(output_folder, exist_ok=True)
    try:
        # Download as mp4
        title = replace_forbidden_characters(data['title'] + ".mp4")
        print(f"Downloading Title: {title}")
        data['stream'].download(filename = title, output_path = output_folder)
        mp4 = os.path.join(output_folder, title)
        mp3 = os.path.join(output_folder, title[:-1] + '3')
        # Convert to mp3
        audio_clip = AudioFileClip(mp4)
        audio_clip.write_audiofile(mp3)
        audio_clip.close()
        os.remove(mp4)
    except Exception as err:
        print(f"Inner error while downloading or converting {data['title']} to mp3 with {err}")


def replace_forbidden_characters(filename):
    forbidden_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in forbidden_characters:
        filename = filename.replace(char, '_')
    return filename