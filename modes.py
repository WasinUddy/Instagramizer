import tkinter as tk
from tkinter import filedialog

from functions import *

class Mode_0:
    """
    Import Mode
    """
    def __init__(self, data: list):
        self.data = data

    def interact(self):
        """
        Import Images
        """
        self.data[0] = filedialog.askopenfilenames(initialdir = "/", title = "Select Images", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

    def up(self):
        pass

    def down(self):
        pass


class Mode_1:
    """
    Color Selection Mode
    """
    def __init__(self, data: list):
        self.data = data

    def interact(self):
        pass

    def up(self):
        self.data[0] = bound(self.data[0] - 1, 0, 6)

    def down(self):
        self.data[0] = bound(self.data[0] + 1, 0, 6)


class Mode_2:
    """
    Export Mode
    """
    COLORS = {
        0: (0, 0, 255),
        1: (0, 255, 0),
        2: (0, 255, 255),
        3: (255, 0, 0),
        4: (255, 0, 255),
        5: (255, 255, 0),
        6: (255, 255, 255)
    }
    def __init__(self, data: list):
        self.data = data

    def interact(self, photos, color):
        export_folder = filedialog.askdirectory(initialdir = "/", title = "Select Export Folder")
        print(photos)
        print(color)
        for i in range(len(photos)):
            add_border(photos[i], export_folder, self.COLORS[color])
    def up(self):
        pass

    def down(self):
        pass