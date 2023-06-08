from PIL import Image, ImageTk
from customtkinter import filedialog

import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def gifload():
    gif_file = filedialog.askopenfilename(title = 'Select image',filetypes=((("GIF File","*.gif"),)))
    if gif_file == '':
        return 'Error'
    else:
        return gif_file

def resize_image(image, width, height):
    image_orig = Image.open(image)
    image = image_orig.resize((width,height), Image.ADAPTIVE)
    image = ImageTk.PhotoImage(image=image)
    return image

def imagefile(file):
    imagefile = ImageTk.PhotoImage(file=file)
    return imagefile

def image_tray(file):
    image_tray_ico = Image.open(file)
    return image_tray_ico

def load_image():
    image = filedialog.askopenfilename(title = 'Select image',filetypes=((("PNG File","*.png"), ("JPEG File","*.jpg"))))
    if image == '':
        return 'Error'
    else:
        return image
    


