import os
from datetime import datetime
from moviepy.editor import AudioFileClip

def convert_to_mp3(audio_data, playlist_title):
    output_folder = os.path.join("./out", playlist_title)
    os.makedirs(output_folder, exist_ok=True)
    for idx, data in enumerate(audio_data, start=1):
        try:
            # Download as mp4
            title = replace_forbidden_characters(data['title'] + ".mp4")
            print(f"Title: {title}")
            data['stream'].download(filename = title, output_path = output_folder)
            print(f"Downloaded MP4 {idx}/{len(audio_data)}")
            mp4 = os.path.join(output_folder, title)
            mp3 = os.path.join(output_folder, title[:-1] + '3')
            # Convert to mp3
            audio_clip = AudioFileClip(mp4)
            audio_clip.write_audiofile(mp3)
            audio_clip.close()
            os.remove(mp4)
            print(f"Converted MP3 {idx}/{len(audio_data)}")
        except Exception as err:
            print(f"Error while downloading or converting {data['title']} to mp3 with {err}")


def replace_forbidden_characters(filename):
    forbidden_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in forbidden_characters:
        filename = filename.replace(char, '_')
    return filename