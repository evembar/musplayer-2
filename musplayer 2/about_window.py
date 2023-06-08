from customtkinter import CTkToplevel, CTkLabel
import modules.imager as imager
import modules.configer as configer
import modules.lang as lang

theme = configer.apperiance()

if theme == 'black':
    theme = 'white'
elif theme == 'white':
    theme = 'black'

import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def about_mus():
    desi = CTkToplevel()

    desi.title(lang.lang_system['about'])
    desi.geometry('350x500')
    desi.resizable(width=False, height=False)

    logo_empty_album_photoi = imager.imagefile(file = 'src/bibs.png')

    logo_empty_album_i = CTkLabel(desi, text = '', image = logo_empty_album_photoi)
    logo_empty_album_i.place(x = -30, y = 20)

    tree = 'Release bib'

    version = 1.0
    make_by = lang.lang_system['make by']

    text_versioni = CTkLabel(desi, text = f'{tree}\n{version}\n{make_by}\nWebMast\nWebAnLiMaks\n2023', text_color=theme, font=('Segoe UI Light', 20 ))
    text_versioni.place(x = 100, y = 250)

    desi.focus_set()

    desi.mainloop()
