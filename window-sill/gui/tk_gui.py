"""
Tkinter GUI

REFERENCES
https://docs.python.org/3/library/tkinter.html#a-simple-hello-world-program
"""
import tkinter as tk

import config


class ApplicationGUI(tk.Frame):
    def __init__(self, **options):
        title = options.get('title', config.app.TITLE)
        width = options.get('width', config.app.WIDTH)
        height = options.get('height', config.app.HEIGHT)

        self.window = tk.Tk()
        super().__init__(self.window)

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.set_title(title)
        self.set_window_size(width, height)

    def set_title(self, title):
        self.window.title(title)
        return self

    def set_window_size(self, width, height):
        geometry_f = "{w}x{h}+{x}+{y}"
        x = int((self.screen_width/2) - (width/2))
        y = int((self.screen_height/2) - (height/2))

        geometry = geometry_f.format(w=width, h=height, x=x, y=y)
        self.window.geometry(geometry)
        return self
