import modules.configer as configer
from customtkinter import CTk, CTkLabel
from sys import exit 
from tkinter import PhotoImage
import modules.musicer as musicer
import modules.lang as lang

conf = configer.get_config_info()

des = CTk()
screenw = ((des.winfo_screenwidth())/100)*50
screenh = ((des.winfo_screenheight())/100)*50

des.geometry(f'{conf[0]}x{conf[1]}')
des.resizable(width=False, height=False)
des.title('')

import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def on_closing():
    exit()



apperiance = configer.apperiance()
if apperiance == 'black':
    logo = PhotoImage(file=f'src/icon/icon_white.png')
    webanlimaks_logo_image = PhotoImage(file=f'src/icon/logo_webanlimaks_black.png')
    des.configure(fg_color = 'black')
    colorfont = 'white'
elif apperiance == 'white':
    logo = PhotoImage(file=f'src/icon/icon_black.png')
    webanlimaks_logo_image = PhotoImage(file=f'src/icon/logo_webanlimaks_white.png')
    des.configure(fg_color = 'white')
    colorfont = 'black'

image = CTkLabel(des, text='', image=logo)
image.place(x = (conf[0]/2)-55, y = (conf[1]/2)-100)

webanlimaks_logo = CTkLabel(des, text='', image=webanlimaks_logo_image)
webanlimaks_logo.place(x = ((conf[0]/100)*78), y = ((conf[1]/100)*75))

text_loading = CTkLabel(des, text=lang.lang_system['loading musplayer 2'], text_color=colorfont, font=('Segoe UI Light', 25))
text_loading.place(x = (conf[0]/2)-75, y = (conf[1]/2+25))

des.protocol("WM_DELETE_WINDOW", on_closing)

musicer.startup_sound('src/sound/weban.mp3')

des.after(2000, des.destroy)

des.mainloop()

import main


