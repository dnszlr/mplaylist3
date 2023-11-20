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

- Install [*pyinstaller*](https://pypi.org/project/pyinstaller/)
    ```bash
    pip install pyinstaller
    ```

- Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

## How to Use (from project root folder)

1. **Build the Executable:**

    ```bash
    pyinstaller ./mpl3.spec
    ```

2. **Run the Executable:**

   - Navigate to the `dist` directory:

     ```bash
     cd dist
     ```

   - Run the executable file (replace `mpl3` with the name of your script):

     ```bash
     ./mpl3.exe
     ```

3. **Enter a Playlist URL:**

   - Paste the URL of your desired YouTube playlist.

4. **Choose an Option:**

   - **Press "Preview"** to display the songs in the playlist. Select specific songs and proceed to download.

   - **Click "Download"** to download selected (or all if nothing got selected) songs in the playlist (can be used without creating a **Preview**).

   - **Select "Playlists"** to access the directory on your computer containing all downloaded playlists.

5. **Enjoy your downloaded playlist!**

## Contributors

- Dennis ([@dnszlr](https://github.com/dnszlr))