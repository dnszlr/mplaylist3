# mplaylist3

## Introduction

This Python script allows you to download videos from a YouTube (single video or playlist) and convert them to MP3 audio format. It uses the pytube and moviepy libraries for video downloading and conversion.

## Prerequisites

- Install [*Python 3.x*](https://www.python.org/downloads/)

- Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

## How to use (Paths from root folder)

1. **Build the Executable:**
    ```bash
    pyinstaller ./mpl3.spec
    ```

2. **Run the application:**

    1. **Via Executable:**
        - Navigate to the [dist](./dist/) directory:
        ```bash
        cd dist
        ```

        - Run the executable file:
        ```bash
        ./mpl3.[extension]
        ```

    2. **Via python script**
        - Run the [mpl3.py](./mpl3.py) script:
        ```bash
        python mpl3.py
        ```

3. **Enter a Playlist URL:**

   - Paste the URL of your desired YouTube playlist.

4. **Choose an Option:**
    - **Select "Download Folder"** to open the folder your downloaded songs or playlists are saved in.

    - **Press "Preview"** to display the songs in the playlist. Select specific songs and proceed to download.

    - **Click "Reset** to reset the currently previewed video or playlist.

    - **Click "Download"** to download selected (or all if nothing got selected) songs in the playlist (can be used without creating a **Preview**).

    - **Select "Playlists"** to access the directory on your computer containing all downloaded playlists.

5. **Enjoy your downloaded playlist!**

## Contributors

- Dennis ([@dnszlr](https://github.com/dnszlr))