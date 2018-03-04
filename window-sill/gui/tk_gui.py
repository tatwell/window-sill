"""
Tkinter GUI

REFERENCES
https://docs.python.org/3/library/tkinter.html#a-simple-hello-world-program
"""
import tkinter as tk

import config


class ApplicationGUI(tk.Frame):
    def __init__(self, **options):
        self.title = options.get('title', config.app.TITLE)
        self.width = options.get('width', config.app.WIDTH)
        self.height = options.get('height', config.app.HEIGHT)

        self.window = tk.Tk()
        super().__init__(self.window)

        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        self.set_title(self.title)
        self.set_window_size(self.width, self.height)
        self.init_buttons()

    def init_buttons(self):
        """Try to create a simple button group that fills full window. This seems
        to be stupidly difficult in Tkinter.

        Based on https://stackoverflow.com/a/7591453/1093087.
        """
        sticky = tk.N + tk.S + tk.E + tk.W
        button_frame = tk.Frame(self.window)
        button_frame.grid(row=0, column=0, sticky=sticky)
        button_frame.rowconfigure(0, weight=1)
        button_frame.columnconfigure(0, weight=1)

        def button(label):
            weight = 16
            height = 10
            color = label.lower()
            callback = lambda: self.window.configure(background=color)
            return tk.Button(button_frame, text=label, width=weight, height=height,
                             background=color, command=callback)

        self.red_button = button('Red').grid(row=0, column=0)
        self.yellow_button = button('Yellow').grid(row=0, column=1)
        self.green_button = button('Green').grid(row=0, column=2)

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
