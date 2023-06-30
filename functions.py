import tkinter as tk
from tkinter import filedialog
import os

from PIL import Image
import cv2


def bound(x, a, b):
    if x < a:
        return a
    elif x > b:
        return b
    else:
        return x
    
def name_limit(char_length, name):
    if '/' in name:
        name = name.split('/')[-1]
    elif '\\' in name:
        name = name.split('\\')[-1]
    if len(name) < char_length:
        return name 
    else:
        return name[:char_length]

def add_border(image_path, export_folder, bg_color):
    print(image_path)
    image_name = os.path.basename(image_path)
    image = cv2.imread(image_path)
    h, w, c = image.shape
    size = max(h, w)

    # Construct New Image
    new_image = Image.new('RGB', (size, size), color = bg_color)
    offset = (int((size - w) / 2), int((size - h) / 2))
    new_image.paste(Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), offset)
    export_path = os.path.join(export_folder, image_name)
    # Resize 1080x1080
    new_image = new_image.resize((1080, 1080))

    # Save Image
    new_image.save(export_path)
    
    print("Exported: " + export_path)