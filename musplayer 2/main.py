from tkinter import PhotoImage
import customtkinter
import os.path
import modules.musicer as musicer
from moviepy.editor import AudioFileClip
from taglib import File
from CTkMessagebox import CTkMessagebox
import modules.imager as imager
import about_window
import modules.configer as configer
from sys import exit
import modules.trayer as trayer
import modules.lang as lang

try:
    import cfg
except:
    import settings
    settings.error_situs = True
    settings.errorring()
    settings.setting()

music_filename = ''

colormode = configer.apperiance()

play_process = False

repeat_mode = False

playlist_mode = False

default_theme = cfg.theme

des = customtkinter.CTk()

des.geometry('740x350')
des.resizable(width=False, height=False)
des.title('musplayer 2')

import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class MainAPI:
    def version():
        print('musplayer 2 0.08\nAPI ver. 0.01')
    def icon_theme(name):
        global default_theme
        default_theme = name
    def play():
        play_object()
    def stop():
        stop_object()

class tray_manager:
    global text_artist_name, text_music_name
    def return_des():
        des.deiconify()
    def minimize_des():
        des.withdraw()
    def exiting():
        exit()
    def play():
        play_object()
    def repeat():
        repeat_toggle()
    def pause():
        pause_object()
    def load_music():
        global text_artist_name, text_music_name
        open_extract_audio()
        return f'{text_artist_name._text} - {text_music_name._text}'
    def stop():
        stop_object()
    def duration_minus():
        minus_time_object()
    def duration_plus():
        plus_time_object()

def settings_object():
    import settings
    settings.setting()

def on_closing():
    msg = CTkMessagebox(title="musplayer 2", message=lang.lang_system['program ask'],
                        icon="question", option_1=lang.lang_system['minimize tray'], 
                        option_2=lang.lang_system['exit'], option_3=lang.lang_system['continue session'],
                        width=lang.lang_system['wwindow'])
    
    if msg.get() == lang.lang_system['minimize tray']:
        tray_manager.minimize_des()
        try:
            tray = trayer.TRAY(color = colormode)
            des.after(200, lambda: tray.active_tray_mod(labeltext=f'{text_artist_name._text} - {text_music_name._text}') )
        except:
            CTkMessagebox(title='musplayer 2', message=lang.lang_system['theme error'])
            tray_manager.return_des()
        
    elif msg.get() == lang.lang_system['exit']:
        exit()

def play_with_playlist(name,path, title, artist):
    des.title(name)
    text_music_name.configure(text=title)
    text_artist_name.configure(text=artist)
    musicer.playlist_file(path=path)
    des.after(100, play_object)

def add_playlistier(name, path, title, artist):
    container_for_object_playlist = [name, path, title, artist]
    playlist_object = customtkinter.CTkButton(playlist_box,  text= container_for_object_playlist[0], text_color=colorfont, fg_color='transparent', hover_color=color_progressbar[1], height = 8,command=lambda: play_with_playlist(name = container_for_object_playlist[0],
                                                                                                                                     path = container_for_object_playlist[1],
                                                                                                                                     title = container_for_object_playlist[2],
                                                                                                                                     artist = container_for_object_playlist[3]))
    playlist_object.pack(pady=3)

def get_playlistier():
    global playlist_mode

    if playlist_mode == False:
        playlist_mode = True
        des.geometry('740x570')
    elif playlist_mode == True:
        playlist_mode = False
        des.geometry('740x350')

    
def open_video_plugin():
    import vider
    video_plugin = vider.VIDEO()
    des.focus_displayof()

def bg_image_load():
    bg_image = imager.load_image() 
    if bg_image == 'Error':
        pass
    else:
        image_panel = imager.resize_image(image = bg_image, width=740, height=350)
        image_background.configure(image = image_panel)   

def load_image():
    image = imager.load_image()
    if image == 'Error':
        pass
    else:
        image_panel = imager.resize_image(image = image, width=100, height=100)
        logo_empty_album_.configure(image = image_panel)

def about_mus():
    about_window.about_mus()
    des.focus_displayof()

def minus_time_object():
    musicer.minus_time()

def plus_time_object():
    musicer.plus_time()

def pause_object():
    global play_process
    play_process = False
    musicer.pause()

def play_duration_process():
    global play_process
    if music_filename == '':
        raise Warning('Music is not loaded')
    else:

        mn, sc = divmod(duration, 60)
        hr, mn = divmod(mn, 60)

        us_converted_time = f"{hr}:{mn}:{sc}"

        converted_time = musicer.process_music()

        progressbar_duration_music.set((duration - (duration - converted_time[2]))/duration)

        text_duration_music.configure(text=us_converted_time + f'\n{converted_time[0]}')
        if converted_time[1] == True:
            text_duration_music.after(100,play_duration_process)
        elif converted_time[1]== False:
            progressbar_duration_music.set(0)
            play_process = False
            text_duration_music.configure(text=lang.lang_system['its music time'])



def open_extract_audio():
    global music_filename, path_music_filename, play_process
    play_process = False
    music_filename = musicer.file()
    path_music_filename = music_filename[1]

    tag = File(music_filename[0])
    try:
        title = tag.tags['TITLE']
        text_music_name.configure(text=tag.tags['TITLE'])
        text_duration_music.configure(text=lang.lang_system['its music time'])
    except:
        music_filename = os.path.basename(music_filename[0])
        title = music_filename
        text_music_name.configure(text=music_filename)
        text_duration_music.configure(text=lang.lang_system['its music time'])

    try:
        artist = tag.tags['ARTIST']
        text_artist_name.configure(text=tag.tags['ARTIST'])
    except:
        artist = lang.lang_system['unknown']
        text_artist_name.configure(text = lang.lang_system['unknown'])

    des.title(f'{artist} - {title}')    

    text_duration_music.configure(text=lang.lang_system['its music time'])
    progressbar_duration_music.set(0)
    add_playlistier(name=f'{artist} - {title}', path=path_music_filename, title=title, artist=artist)

def repeat_toggle():
    global repeat_mode, play_process
    if repeat_mode == False:
        musicer.stop()
        repeat_mode = True
        play_process = False
        CTkMessagebox(title="musplayer", message=lang.lang_system['repeat mode on'])
    elif repeat_mode == True:
        musicer.stop()
        repeat_mode = False
        play_process = False
        CTkMessagebox(title="musplayer", message=lang.lang_system['repeat mode off'])


def play_object():
    global duration, play_process
    if music_filename == '':
        raise Warning('Music is not loaded')
    else:
        play_ready = musicer.play(repeat_mode=repeat_mode)
        if play_ready == 'Error':
            pass
        else:
            if play_process == False:
                duration = int(AudioFileClip(path_music_filename).duration)
                play_duration_process()
                play_process = True
            elif play_process == True:
                pass


def stop_object():
    global play_process
    musicer.stop()
    text_duration_music.configure(text="It's music\ntime")
    play_process = False
    progressbar_duration_music.set(0)

if colormode == "black":
    try:
        logo_empty_album_color = PhotoImage(file = f'src/{default_theme}/black/logo_empty_album.png')
        colorfont = 'white'
        color_progressbar = ['white', 'black']
        load_music = PhotoImage(file = f'src/{default_theme}/black/load_music.png')
        load_video = PhotoImage(file = f'src/{default_theme}/black/load_video.png')
        settings = PhotoImage(file=f'src/{default_theme}/black/settings.png')
        about = PhotoImage(file=f'src/{default_theme}/black/about.png')
        duration_minus = PhotoImage(file = f'src/{default_theme}/black/duration_minus.png')
        duration_plus = PhotoImage(file = f'src/{default_theme}/black/duration_plus.png')
        playlist = PhotoImage(file = f'src/{default_theme}/black/playlist.png')
        pause = PhotoImage(file=f'src/{default_theme}/black/pause.png')
        play = PhotoImage(file=f'src/{default_theme}/black/play.png')
        stop = PhotoImage(file=f'src/{default_theme}/black/stop.png')
        repeat = PhotoImage(file=f'src/{default_theme}/black/repeat.png')
        gif = PhotoImage(file=f'src/{default_theme}/black/image_load.png')
    except:
        import settings
        settings.error_situs = True
        settings.errorring()
        settings.setting()
elif colormode == 'white':
    try:
        logo_empty_album_color = PhotoImage(file = f'src/ui/white/logo_empty_album.png')
        colorfont = 'black'
        color_progressbar = ['black', 'white']
        load_music = PhotoImage(file=f'src/{default_theme}/white/load_music.png')
        load_video = PhotoImage(file = f'src/{default_theme}/white/load_video.png')
        settings = PhotoImage(file=f'src/{default_theme}/white/settings.png')
        about = PhotoImage(file=f'src/{default_theme}/white/about.png')
        duration_minus = PhotoImage(file=f'src/{default_theme}/white/duration_minus.png')
        duration_plus = PhotoImage(file=f'src/{default_theme}/white/duration_plus.png')
        playlist = PhotoImage(file=f'src/{default_theme}/white/playlist.png')
        pause = PhotoImage(file=f'src/{default_theme}/white/pause.png')
        play = PhotoImage(file=f'src/{default_theme}/white/play.png')
        stop = PhotoImage(file=f'src/{default_theme}/white/stop.png')
        repeat = PhotoImage(file=f'src/{default_theme}/white/repeat.png')
        gif = PhotoImage(file=f'src/{default_theme}/white/image_load.png')
    except:
        import settings
        settings.error_situs = True
        settings.errorring()
        settings.setting()

image_background = customtkinter.CTkLabel(des, text = '', image = '', fg_color='transparent', width=10)
image_background.place(x = 0, y = 0)

logo_empty_album_ = customtkinter.CTkButton(des, text = '', image = logo_empty_album_color, fg_color='transparent', width=10, hover_color=color_progressbar[1], command=load_image)
logo_empty_album_.place(x = 13, y = 20)

text_music_name = customtkinter.CTkLabel(des, text=lang.lang_system['music name'], text_color=colorfont, font= ('Segoe UI Light', 20), fg_color='transparent', wraplength=600 )
text_music_name.place(x = 140, y = 30)

text_artist_name = customtkinter.CTkLabel(des, text=lang.lang_system['artist name'], text_color=colorfont, font= ('Segoe UI Light', 20), fg_color='transparent' )
text_artist_name.place(x = 140, y = 80)

text_duration_music = customtkinter.CTkLabel(des, text=lang.lang_system['its music time'], text_color=colorfont, font= ('Segoe UI Light', 20), fg_color='transparent' )
text_duration_music.place(x = 20, y = 150)

progressbar_duration_music = customtkinter.CTkProgressBar(des, width=520,  progress_color=color_progressbar[0], border_color=color_progressbar[1],   mode='determinate')
progressbar_duration_music.place(x = 110, y = 170)
progressbar_duration_music.set(0)

button_load_music = customtkinter.CTkButton(des, text = '', image=load_music, fg_color='transparent', hover_color=color_progressbar[1],  width=50, height=50, command=open_extract_audio)
button_load_music.place(x = 20, y = 220)

button_load_video = customtkinter.CTkButton(des, text = '', image=load_video, fg_color='transparent', hover_color=color_progressbar[1],  width=50, height=50, command=open_video_plugin)
button_load_video.place(x = 20, y = 280)

button_gif = customtkinter.CTkButton(des, text = '', image=gif, fg_color='transparent', hover_color=color_progressbar[1],  width=50, height=50, command=bg_image_load)
button_gif.place(x = 650, y = 160)

button_settings = customtkinter.CTkButton(des, text = '', image=settings, fg_color='transparent', hover_color=color_progressbar[1],  width=50, height=50, command=settings_object)
button_settings.place(x = 650, y = 220)

button_about = customtkinter.CTkButton(des, text = '', image=about, fg_color='transparent', hover_color=color_progressbar[1],  width=50, height=50, command=about_mus)
button_about.place(x = 650, y = 280)

button_duration_minus = customtkinter.CTkButton(des, text = '', image=duration_minus, fg_color='transparent', hover_color=color_progressbar[1],  width=50, height=50, command=minus_time_object)
button_duration_minus.place(x = 90, y = 245)

button_duration_plus = customtkinter.CTkButton(des, text = '', image=duration_plus, fg_color='transparent', hover_color=color_progressbar[1],  width=50, height=50, command=plus_time_object)
button_duration_plus.place(x = 530, y = 245)

button_playlist = customtkinter.CTkButton(des, text = '', image=playlist, fg_color='transparent', hover_color=color_progressbar[1],  width=50, height=50, command = get_playlistier)
button_playlist.place(x = 203, y = 245)

button_pause = customtkinter.CTkButton(des, text = '', image=pause, fg_color='transparent', hover_color=color_progressbar[1],  width=50, height=50, command=pause_object)
button_pause.place(x = 270, y = 245)

button_play = customtkinter.CTkButton(des, text = '', image=play, fg_color='transparent', hover_color=color_progressbar[1],  width=50, height=50, command=play_object)
button_play.place(x = 333, y = 245)

button_stop = customtkinter.CTkButton(des, text = '', image=stop, fg_color='transparent', hover_color=color_progressbar[1],  width=50, height=50, command=stop_object)
button_stop.place(x = 400, y = 245)

button_repeat = customtkinter.CTkButton(des, text = '', image=repeat, fg_color='transparent', hover_color=color_progressbar[1],  width=50, height=50, command=repeat_toggle)
button_repeat.place(x = 463, y = 245)

playlist_box = customtkinter.CTkScrollableFrame(des, width=680, height = 180, orientation='vertical')
playlist_box.place(x=20,y=350)

des.protocol("WM_DELETE_WINDOW", on_closing)



des.mainloop()