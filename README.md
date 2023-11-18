# mplaylist3

## Introduction

This Python script allows you to download videos from a YouTube playlist and convert them to MP3 audio format. It uses the pytube and moviepy libraries for video downloading and conversion.

## Prerequisites

- Install [*Python 3.x*](https://www.python.org/downloads/)
- Install [*pytube*](https://pypi.org/project/pytube/)
    ```bash
    pip install pytube
    ```
- Install [*moviepy*](https://pypi.org/project/moviepy/)
    ```bash
    pip install moviepy
    ```
- Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

## How to Use

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the script with the playlist URL:

    ```bash
    python mpl3.py <playlist_url>
    ```

    Replace `<playlist_url>` with the URL of the YouTube playlist you want to download.

3. The script will save the MP3 files in the **out** folder. In there you can find the name of your playlist.

## Contributors

- Your Name Dennis (@dnszlr)