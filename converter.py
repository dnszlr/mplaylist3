from file_handling import get_root_folder
from moviepy.editor import AudioFileClip
import os, logger as Logger

def convert_to_mp3(video, title):
    output_folder = os.path.join(get_root_folder(), "out")
    data_folder = os.path.join(output_folder, title)
    os.makedirs(data_folder, exist_ok=True)
    try:
        # Download as mp4
        video.title = replace_forbidden_characters(video.title + ".mp4")
        video.title = filter_non_ascii(video.title)
        Logger.info(f"Starting download of {video.title} ")
        video.stream.download(filename = video.title, output_path = data_folder)
        mp4 = os.path.join(data_folder, video.title)
        mp3 = os.path.join(data_folder, video.title[:-1] + '3')
        Logger.info(f"Starting converting from {mp4} to {mp3}")
        # Convert to mp3
        audio_clip = AudioFileClip(mp4)
        audio_clip.write_audiofile(mp3)
        audio_clip.close()
        Logger.info(f"Deleting Video file {mp4}")
        os.remove(mp4)
    except Exception as err:
        Logger.error(f"Error while downloading or converting {video.title} to mp3 with {err}")

def replace_forbidden_characters(title):
    forbidden_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in forbidden_characters:
        title = title.replace(char, '_')
    return title

def filter_non_ascii(title):
    return title.encode('ascii', 'ignore').decode('ascii')