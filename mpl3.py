from file_handling import get_root_folder, is_exe
from playlist_parser import get_playlist, get_videos, get_video_streams
import sys, os, threading, logging, tkinter as tk
from converter import convert_to_mp3
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

class MPL3:
    def __init__(self, master):

        # Set up master
        self.master = master
        self.master.title("MPL3 YouTube Playlist Downloader")
        self.master.geometry("800x600")

        # Data storage
        self.video_storage = []

        # Playlist Link Entry
        self.playlist_label = tk.Label(master, text="Enter Playlist URL:")
        self.playlist_label.pack()

        self.playlist_entry = tk.Entry(master)
        self.playlist_entry.pack(fill=tk.X)

        # Playlist Listbox
        self.playlist_label = tk.Label(master, text="Playlist")
        self.playlist_label.pack()
        self.playlist_listbox = tk.Listbox(master, selectmode=tk.MULTIPLE)
        self.playlist_listbox.pack(expand=True, fill=tk.BOTH)

        # Progress Bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(root, variable=self.progress_var)
        self.progress_bar.pack(fill=tk.BOTH)

        # File Button
        self.explorer_button = tk.Button(master, text="Playlists", width=20, command=self.open_files)
        self.explorer_button.pack(side='left', anchor='e')
        # Download Button
        self.download_button = tk.Button(master, text="Download", width=20, command=self.start_download)
        self.download_button.pack(side='right', anchor='w')
        # Preview Button
        self.preview_button = tk.Button(master, text="Preview", width=20, command=self.start_preview)
        self.preview_button.pack(side='right', anchor='w')

    def preview_playlist(self):
        playlist_url = self.playlist_entry.get()
        playlist = get_playlist(str(playlist_url))
        if playlist_url and playlist:
            root.config(cursor="watch")
            self.playlist_label.config(text=playlist.title)
            videos = get_videos(playlist)
            for idx, video in enumerate(videos, start=1):
                self.increase_process_value((idx / len(videos)) * 100)
                if video not in self.video_storage:
                    title = video.title
                    self.video_storage.append(video)
                    self.playlist_listbox.insert(tk.END, title)
            self.increase_process_value(0)
            root.config(cursor="")
        else:
            messagebox.showerror("Playlist Not Found", "Provide a valid URL for a publicly accessible playlist.")

    def download_playlist(self):
        selected_titles = [self.playlist_listbox.get(idx) for idx in self.playlist_listbox.curselection()]
        if len(selected_titles) == 0:
            selected_titles = self.get_selected_titles()
        if len(selected_titles) == 0:
            self.preview_playlist()
            selected_titles = self.get_selected_titles()
        root.config(cursor="watch")
        self.increase_process_value(1)
        selected_videos = [video for video in self.video_storage if video.title in selected_titles]
        streams = get_video_streams(selected_videos)
        playlist_title = self.playlist_label.cget("text")
        for idx, stream in enumerate(streams, start=1):
            print(f"Steam is: {stream}")
            try:
                convert_to_mp3(stream, playlist_title)
            except Exception as err:
                logging.debug(f"Outer error while downloading or converting {stream['title']} to mp3 with {err}")
            self.increase_process_value((idx / len(streams)) * 100)
        messagebox.showinfo("Completion", "The download process has been completed.")
        root.config(cursor="")
        self.increase_process_value(0)

    def open_files(self):
        out_directory = os.path.join(get_root_folder(), "out")
        if sys.platform.startswith('win'):
            os.system(f'explorer {out_directory}')
        elif sys.platform.startswith('darwin'):
            os.system(f'open {out_directory}')
        elif sys.platform.startswith('linux'):
            os.system(f'xdg-open {out_directory}')
        else:
            message = "Unsupported platform for file opening."
            logging.debug(message)
            messagebox.showerror(message)

    def get_selected_titles(self):
        return [self.playlist_listbox.get(idx) for idx in range(self.playlist_listbox.size())]

    def start_preview(self):
        preview_thread = threading.Thread(target=self.preview_playlist)
        preview_thread.start()

    def start_download(self):
        download_thread = threading.Thread(target=self.download_playlist)
        download_thread.start()

    def increase_process_value(self, progress_value):
        self.progress_var.set(progress_value)
        root.update_idletasks()

if __name__ == "__main__":
    logging.basicConfig(filename='debug.log', 
                        level=logging.DEBUG, 
                        format='%(asctime)s [%(levelname)s]: %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S')
    executed_as_exe = is_exe()
    # Don't delete me, moviepy needs something to write to if no console is present
    temp_output_path = os.path.join(get_root_folder(), "output.txt")
    if executed_as_exe:
        temp_output_file = open(temp_output_path, "wt")
        sys.stdout = temp_output_file
        sys.stderr = temp_output_file
    root = tk.Tk()
    app = MPL3(root)
    im = Image.open('./assets/mpl3.ico')
    icon = ImageTk.PhotoImage(im)
    root.wm_iconphoto(True, icon)
    root.mainloop()
    if executed_as_exe:
        os.remove(temp_output_path)