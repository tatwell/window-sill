from tkinter import Tk

import config


class TinkerGUI(object):
    def __init__(self, **options):
        title = options.get('title', config.app.TITLE)

        self.window = self._init_window()
        self.set_title(title)

    def loop(self):
        self.window.mainloop()

    def set_title(self, title):
        self.window.title(title)

    def _init_window(self):
        return Tk()
