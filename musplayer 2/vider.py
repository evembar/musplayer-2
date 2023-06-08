from customtkinter import CTkToplevel, CTkButton, CTkLabel, filedialog
from tkinter import PhotoImage
import modules.configer as configer
from tkVideoPlayer import TkinterVideo
import os
from CTkMessagebox import CTkMessagebox
from moviepy.editor import VideoFileClip
import modules.lang as lang

try:
    import cfg
except:
    import fataler

import sys
import os

default_theme=cfg.theme

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class VIDEO:
    def __init__(self):
        
        self.repeat_mode = False

        self.des = CTkToplevel()
        self.des.title(lang.lang_system['vider title'])
        self.des.geometry(f'{configer.width_window}x{configer.height_window}')

        def load_video_file():
            if os.path.isfile('file_convert.mp3'):
                os.remove('file_convert.mp3')
            else:
                pass
            video_file = filedialog.askopenfilename(title='Select of video files', filetypes=(('MP4 Files', '*.mp4'), ('AVI Files', '*avi')))
            self.des.focus_force()
            base_video_file_name = os.path.basename(video_file)
            self.text_name_video.configure(text=lang.lang_system['please wait'])
            self.video_screen.load(video_file)
            self.des.update()
            clip = VideoFileClip(video_file)
            clip.audio.write_audiofile(f"file_convert.mp3")
            self.text_name_video.configure(text=base_video_file_name)
            self.des.update()



        def repeat():
            if self.repeat_mode == False:
                self.video_screen.stop()
                self.repeat_mode = True
                CTkMessagebox(title="vider", message=lang.lang_system['repeat mode on'])
            elif self.repeat_mode == True:
                self.video_screen.stop()
                self.repeat_mode = False
                CTkMessagebox(title="vider", message=lang.lang_system['repeat mode off'])

        def video_ended(event):
            if self.repeat_mode == True:
                self.video_screen.play()
            elif self.repeat_mode == False:
                pass

        def skip(value: int):
            """ skip seconds """
            self.video_screen.seek(int(self.video_screen.current_duration())+value)

        def video_play_file():
            self.video_screen.play()

        def video_pause_file():
            self.video_screen.pause()

        def video_stop_file():
            self.video_screen.stop()

        self.colormode = configer.apperiance()
        print(self.colormode)
        if self.colormode == "black":
            self.colorfont = 'white'
            self.colortheme = 'black'
            self.vload_video = PhotoImage(file = f'src/{default_theme}/black/load_video.png')
            self.vduration_minus = PhotoImage(file = f'src/{default_theme}/black/duration_minus.png')
            self.vduration_plus = PhotoImage(file = f'src/{default_theme}/black/duration_plus.png')
            self.vpause = PhotoImage(file=f'src/{default_theme}/black/pause.png')
            self.vplay = PhotoImage(file=f'src/{default_theme}/black/play.png')
            self.vstop = PhotoImage(file=f'src/{default_theme}/black/stop.png')
            self.vrepeat = PhotoImage(file=f'src/{default_theme}/black/repeat.png')
        elif self.colormode == 'white':
            self.colorfont = 'black'
            self.colortheme='white'
            self.vload_video = PhotoImage(file = f'src/{default_theme}/white/load_video.png')
            self.vduration_minus = PhotoImage(file=f'src/{default_theme}/white/duration_minus.png')
            self.vduration_plus = PhotoImage(file=f'src/{default_theme}/white/duration_plus.png')
            self.vpause = PhotoImage(file=f'src/{default_theme}/white/pause.png')
            self.vplay = PhotoImage(file=f'src/{default_theme}/white/play.png')
            self.vstop = PhotoImage(file=f'src/{default_theme}/white/stop.png')
            self.vrepeat = PhotoImage(file=f'src/{default_theme}/white/repeat.png')


        self.text_name_video = CTkLabel(self.des, text=lang.lang_system['its video time'], font=('Segoe UI Light', 20), text_color=self.colorfont)
        self.text_name_video.pack()

        self.video_screen = TkinterVideo(self.des, consistant_frame_rate = False)
        self.video_screen.pack(expand = 1, fill='both')

        self.video_duration_minus = CTkButton(self.des, text='', image=self.vduration_minus, fg_color='transparent', hover_color=self.colortheme, width=10, command=lambda: skip(-5))
        self.video_duration_minus.pack(side ='left')

        self.load_video_button = CTkButton(self.des, text='', image=self.vload_video, fg_color='transparent', hover_color=self.colortheme, width=10, command = load_video_file)
        self.load_video_button.pack(side ='left')

        self.video_pause_button = CTkButton(self.des, text='', image = self.vpause, fg_color='transparent', hover_color=self.colortheme, width=10, command=video_pause_file)
        self.video_pause_button.pack(side ='left')

        self.video_play_button = CTkButton(self.des, text='', image=self.vplay, fg_color='transparent', hover_color=self.colortheme, width=10, command=video_play_file)
        self.video_play_button.pack(side = 'left')

        self.video_stop_button = CTkButton(self.des, text='', image=self.vstop, fg_color='transparent', hover_color=self.colortheme, width=10, command=video_stop_file)
        self.video_stop_button.pack(side ='left')

        self.video_repeat_button = CTkButton(self.des, text='', image=self.vrepeat, fg_color='transparent', hover_color=self.colortheme, width=10, command = repeat)
        self.video_repeat_button.pack(side ='left')

        self.video_duration_plus_button = CTkButton(self.des, text='', image=self.vduration_plus, fg_color='transparent', hover_color=self.colortheme, width=10, command=lambda: skip(5))
        self.video_duration_plus_button.pack(side ='left')

        self.video_screen.bind("<<Ended>>", video_ended )

        self.des.focus_force()

        self.des.mainloop()

    

