from customtkinter import filedialog
from pygame import mixer, USEREVENT
import pygame.event
import time

mixer.init()

play_process = None
process_music_duration = False
pause_mod = False
stop_mode = None

flag = 0

import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def stop():
    global play_process
    global pause_mod
    global process_music_duration
    global stop_mode
    
    if play_process == True:
        try:
            mixer.music.stop()
            process_music_duration = False
            play_process = False
        except:
            return 'Error'
    elif play_process == False or play_process == None:
        process_music_duration = False
        if pause_mod == True:
            mixer.music.stop()
            pause_mod = False
            play_process = False
            stop_mode = True
        elif pause_mod == False:
            play_process = False
        return 'Ok'


def playlist_file(path):
    stop()
    mixer.music.load(path)

def startup_sound(file):
    mixer.music.load(file)
    mixer.music.play()

def file():
    global play_process
    global file_music_name
    file_music_name = filedialog.askopenfilename(title = 'Select track',filetypes=((("mp3 Music Files","*.mp3"),("ogg Music Files","*.ogg"), ("wav Music Files", "*.wav"))))
    stop()
    mixer.music.load(file_music_name)
    play_process = False
    return [file_music_name, file_music_name]


def pause():
    global pause_mod
    global play_process
    global stop_mode
    if stop_mode == True:
        pass
    elif stop_mode == None and play_process == True:
            mixer.music.pause()
            pause_mod = True
            play_process = False


def play(repeat_mode):
    global play_process
    global pause_mod
    global flag
    global stop_mode
    flag = 0
    stop_mode = None
    if pause_mod == True:
        pause_mod = False
        play_process = True
        mixer.music.unpause()
    elif pause_mod == False:
        if repeat_mode == True:
            if play_process == False:
                try:
                    play_process = True
                    mixer.music.play(-1)
                except:
                    return 'Error'
            else:
                pass
        elif repeat_mode == False:
            if play_process == False:
                try:
                    play_process = True
                    mixer.music.play()
                except:
                    return 'Error'
            else:
                pass

def custom_init(sequency, buffer, bit, sound):
    mixer.music.stop()
    backup_name_file = file_music_name
    mixer.quit()
    mixer.init(frequency=sequency, size=bit, channels=sound, buffer=buffer)
    mixer.music.load(backup_name_file)

def minus_time():
    global flag
    global raw_time
    if play_process == True:
        flag -=5
        if flag < 0:
            flag = 0

        mixer.music.play(start=flag)
    elif play_process == False or play_process == None:
        raise FutureWarning('file is not playning')

def plus_time():
    global flag
    global raw_time
    if play_process == True:
        flag +=5
        if flag < 0:
            flag = 0
        mixer.music.set_pos(int(raw_time + 5))
        #mixer.music.play(start=flag)
    elif play_process == False or play_process == None:
        raise FutureWarning('file is not playning')

def process_music():
    global process_music_duration 
    global flag
    global play_process
    global raw_time
    raw_time = mixer.music.get_pos()/1000 + flag*60/100
    process_music_duration = True

    converted_time = time.strftime("%H:%M:%S",time.gmtime(raw_time))

    MUSIC_END = USEREVENT+1
    mixer.music.set_endevent(MUSIC_END)

    for event in pygame.event.get():
      if event.type == MUSIC_END:
          process_music_duration = False
          flag = 0
          play_process = False
      else:
          pass
    return [converted_time, process_music_duration, raw_time, flag]

