from customtkinter import CTkToplevel, CTkLabel, CTkButton
from tkinter import PhotoImage
from pystray import Icon, Menu, MenuItem
import modules.imager as imager
try:
    import cfg
except:
    import fataler

import sys
import os

default_theme = cfg.theme_tray

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class TRAY:
    def __init__(self, color):

        from main import tray_manager

        def play_object():
            tray_manager.play()

        def repeat_object():
            tray_manager.repeat()

        def pause_object():
            tray_manager.pause()

        def load_music_object():
            name_title = tray_manager.load_music()
            self.text_duration_music.configure(text=name_title)

        def stop_object():
            tray_manager.stop()

        def duration_minus_object():
            tray_manager.duration_minus()

        def duration_plus_object():
            tray_manager.duration_plus()

        def on_closing():
            self.des.withdraw()
            tray.stop()
            tray_manager.return_des()

        if color == 'black':
            self.color_progressbar = ['white', 'black']
            self.colorfont = 'white'
            self.duration_plus = PhotoImage(file=f'src/{default_theme}/black/duration_plus.png')
            self.duration_minus = PhotoImage(file=f'src/{default_theme}/black/duration_minus.png')
            self.load_music = PhotoImage(file=f'src/{default_theme}/black/load_music.png')
            self.pause = PhotoImage(file=f'src/{default_theme}/black/pause.png')
            self.play = PhotoImage(file=f'src/{default_theme}/black/play.png')
            self.repeat = PhotoImage(file=f'src/{default_theme}/black/repeat.png')
            self.stop = PhotoImage(file=f'src/{default_theme}/black/stop.png')
        else:
            self.color_progressbar = ['black, white']
            self.colorfont = 'black'
            self.duration_plus = PhotoImage(file=f'src/{default_theme}/white/duration_plus.png')
            self.duration_minus = PhotoImage(file=f'src/{default_theme}/white/duration_minus.png')
            self.load_music = PhotoImage(file=f'src/{default_theme}/white/load_music.png')
            self.pause = PhotoImage(file=f'src/{default_theme}/white/pause.png')
            self.play = PhotoImage(file=f'src/{default_theme}/white/play.png')
            self.repeat = PhotoImage(file=f'src/{default_theme}/white/repeat.png')
            self.stop = PhotoImage(file=f'src/{default_theme}/white/stop.png')

        self.des = CTkToplevel()
        self.des.geometry(f'393x78')
        self.des.title('musplayer 2')
        self.des.resizable(width=False, height=False)
        self.des.attributes('-toolwindow', True)


        

        self.des.update()

        self.button_play = CTkButton(self.des, text = '', image=self.play, fg_color='transparent', hover_color=self.color_progressbar[1],  width=25, height=25, command=play_object)
        
        self.button_pause = CTkButton(self.des, text = '', image=self.pause, fg_color='transparent', hover_color=self.color_progressbar[1],  width=25, height=25, command=pause_object)
        
        self.button_repeat = CTkButton(self.des, text = '', image=self.repeat, fg_color='transparent', hover_color=self.color_progressbar[1],  width=25, height=25, command=repeat_object)
        
        self.button_load_music = CTkButton(self.des, text = '', image=self.load_music, fg_color='transparent', hover_color=self.color_progressbar[1],  width=25, height=25, command=load_music_object)
        
        self.button_stop = CTkButton(self.des, text = '', image=self.stop, fg_color='transparent', hover_color=self.color_progressbar[1],  width=25, height=25, command=stop_object)
        
        self.button_duration_minus = CTkButton(self.des, text = '', image=self.duration_minus, fg_color='transparent', hover_color=self.color_progressbar[1],  width=25, height=25, command=duration_minus_object)
        
        self.button_duration_plus = CTkButton(self.des, text = '', image=self.duration_plus, fg_color='transparent', hover_color=self.color_progressbar[1],  width=25, height=25, command=duration_plus_object)
        
        self.text_duration_music = CTkLabel(self.des, text="It's music time!", text_color=self.colorfont, font= ('Segoe UI Light', 20), fg_color='transparent', wraplength= 380)
        
        self.des.protocol("WM_DELETE_WINDOW", on_closing)

        
    def active_tray_mod(self, labeltext):
        from main import tray_manager

        def tray_ico():
            global tray

            def on_closing():
                self.des.withdraw()
                tray.stop()
                tray_manager.return_des()

            a = imager.image_tray('src/icon/icon_white.ico')
            tray = Icon('musplayer 2', a, menu=Menu(
                MenuItem('focus', self.des.focus_force),
                MenuItem('exit', on_closing)
            ))
            tray.run_detached()

        self.text_duration_music.configure(text=labeltext, font= ('Segoe UI Light', 15))

        self.des.after(100, tray_ico)
        self.des.deiconify()
        self.button_play.place(x = 200, y=43)
        self.button_pause.place(x = 157, y=43)
        self.button_repeat.place(x = 240, y=43)
        self.button_load_music.place(x = 115, y=43)
        self.button_stop.place(x = 280, y=43)
        self.button_duration_minus.place(x = 50, y=43)
        self.button_duration_plus.place(x = 320, y=43)
        self.text_duration_music.place(x = 0, y = 5)
        
        self.des.mainloop()
