from tkinter import Tk

import config


class TinkerGUI(object):
    def __init__(self, **options):
        title = options.get('title', config.app.TITLE)
        width = options.get('width', config.app.WIDTH)
        height = options.get('height', config.app.HEIGHT)

        self.window = self._init_window()
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.set_title(title)
        self.set_window_size(width, height)

    def loop(self):
        self.window.mainloop()

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

    def _init_window(self):
        return Tk()
