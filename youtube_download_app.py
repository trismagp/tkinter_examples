#https://www.pythontutorial.net/tkinter/tkinter-example/

from pytube import YouTube
import tkinter as tk
import customtkinter




def download_360p_mp4_videos(url: str, outpath: str = "./"):
    yt = YouTube(url)
    yt.streams.filter(file_extension="mp4").get_by_resolution("360p").download(outpath)
    return yt.title


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simple youtube downloader")
        self.minsize(400, 300)
        customtkinter.set_appearance_mode("dark")
        self.entry = customtkinter.CTkEntry(master=self,
                               placeholder_text="input youtube url",
                               width=520,
                               height=25,
                               border_width=2,
                               corner_radius=10)
        self.entry.pack(padx=20, pady=30)
        self.button = customtkinter.CTkButton(master=self, text="download", command=self.button_callback)
        self.button.pack(padx=5, pady=5)
        self.textbox = customtkinter.CTkTextbox(master=self, width = 520)
        self.textbox.pack( padx=5, pady=10)

    def button_callback(self):
        url = self.entry.get().strip()
        self.entry.delete(0,tk.END)
        self.entry.placeholder_text = "input youtube url"
        
        title = download_360p_mp4_videos(url)
        title = download_360p_mp4_videos(self.entry.get().strip())
        self.textbox.insert("insert",  title + "==>downloaded\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
