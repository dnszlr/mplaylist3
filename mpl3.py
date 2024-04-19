import sys, os, threading, tkinter as tk, logger as Logger
from youtube_parser import get_data_from_url, get_streams
from file_handling import get_root_folder, is_exe
from converter import convert_to_mp3
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

class MPL3:
    def __init__(self, master):

        # Set up master
        self.master = master
        self.master.title("MPL3")
        self.master.geometry("800x600")

        # Data storage
        self.video_storage = []

        # URL
        self.url_label = tk.Label(master, text="Enter playlist or video URL")
        self.url_label.pack()
        self.url_entry = tk.Entry(master)
        self.url_entry.pack(fill=tk.X)

        # Song Listbox
        self.songs_label = tk.Label(master, text="Song titles")
        self.songs_label.pack()
        self.songs_listbox = tk.Listbox(master, selectmode=tk.MULTIPLE)
        self.songs_listbox.pack(expand=True, fill=tk.BOTH)

        # Progress Bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(root, variable=self.progress_var)
        self.progress_bar.pack(fill=tk.BOTH)

        # Buttons
        self.explorer_button = tk.Button(master, text="Download Folder", width=20, command=self.open_files)
        self.explorer_button.pack(side='left', anchor='e')
        self.reset_button = tk.Button(master, text="Reset", width=20, command=self.reset_songs)
        self.reset_button.pack(side='left', anchor='e')
        self.download_button = tk.Button(master, text="Download", width=20, command=self.start_download)
        self.download_button.pack(side='right', anchor='w')
        self.preview_button = tk.Button(master, text="Preview", width=20, command=self.start_preview)
        self.preview_button.pack(side='right', anchor='w')

    def preview(self):
        url = self.url_entry.get()
        wrapper = get_data_from_url(url)
        if url and wrapper:
            self.start_process()
            self.songs_label.config(text=wrapper.title)
            for idx, video in enumerate(wrapper.videos, start=1):
                self.increase_process_value((idx / len(wrapper.videos)) * 100)
                if video not in self.video_storage:
                    title = video.title
                    self.video_storage.append(video)
                    self.songs_listbox.insert(tk.END, title)
            self.stop_process()
        else:
            messagebox.showerror("Videos not found", "Provide a valid URL for a publicly accessible video or playlist and check your internet connection.")

    def download(self):
        selected_titles = [self.songs_listbox.get(idx) for idx in self.songs_listbox.curselection()]
        if len(selected_titles) == 0:
            selected_titles = self.get_selected_titles()
        if len(selected_titles) == 0:
            self.preview()
            selected_titles = self.get_selected_titles()
        self.start_process()
        selected_videos = [video for video in self.video_storage if video.title in selected_titles]
        streams = get_streams(selected_videos)
        title = self.songs_label.cget("text")
        for idx, stream in enumerate(streams, start=1):
            try:
                convert_to_mp3(stream, title)
                messagebox.showinfo("Completion", "The download process has been completed.")
            except Exception as err:
                Logger.error(f"Error while downloading or converting {stream['title']} to mp3 with {err}")
            self.increase_process_value((idx / len(streams)) * 100)
        self.stop_process()

    def open_files(self):
        out_directory = os.path.join(get_root_folder(), "out")
        os.makedirs(out_directory, exist_ok=True)
        Logger.info(f"Directory is {out_directory}")
        if sys.platform.startswith('win'):
            os.system(f'explorer {out_directory}')
        elif sys.platform.startswith('darwin'):
            os.system(f'open {out_directory}')
        elif sys.platform.startswith('linux'):
            os.system(f'xdg-open {out_directory}')
        else:
            message = "Your operating system is not supported."
            Logger.debug(message)
            messagebox.showerror(message)

    def reset_songs(self):
        self.songs_listbox.delete(0,tk.END)
        self.video_storage = []
        self.songs_listbox.config(text='Song titles')

    def get_selected_titles(self):
        return [self.songs_listbox.get(idx) for idx in range(self.songs_listbox.size())]

    def start_preview(self):
        preview_thread = threading.Thread(target=self.preview)
        preview_thread.start()

    def start_download(self):
        download_thread = threading.Thread(target=self.download)
        download_thread.start()

    def increase_process_value(self, progress_value):
        self.progress_var.set(progress_value)
        root.update_idletasks()

    def start_process(self):
        root.config(cursor="watch")
        self.increase_process_value(1)

    def stop_process(self):
        root.config(cursor="")
        self.increase_process_value(0)
        
if __name__ == "__main__":
    executed_as_exe = is_exe()
    # Don't delete, moviepy needs something to write to if no console is present
    temp_output_path = os.path.join(get_root_folder(), "output.txt")
    temp_output_file = None
    if executed_as_exe:
        Logger.configureInfo('info.log')
        temp_output_file = open(temp_output_path, "wt")
        sys.stdout = temp_output_file
        sys.stderr = temp_output_file
    root = tk.Tk()
    app = MPL3(root)
    im = Image.open('./assets/mpl3.ico')
    icon = ImageTk.PhotoImage(im)
    root.wm_iconphoto(True, icon)
    root.mainloop()
    if executed_as_exe and temp_output_file:
        temp_output_file.close()
        os.remove(temp_output_path)