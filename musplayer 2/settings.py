from customtkinter import *
import modules.musicer as muciser
from main import MainAPI
from CTkMessagebox import CTkMessagebox
import modules.lang as lang
import modules.imager as imager
import modules.updater as updater

import sys
import os
import shutil

import wget
from pytube import YouTube
from moviepy.editor import AudioFileClip, VideoFileClip


error_situs = False
lang_var = 'en'
theme_dir = 'ui'
theme_dir_tray = 'tray'
vers = 1.0

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def errorring():
    try:
        import cfg
        error_ui = lang.lang_system['path_src_error']
        msg = CTkMessagebox(width = 550,title='musplayer 2', message=f'{error_ui}{cfg.theme} and {error_ui}{cfg.theme_tray}', 
                    option_1=lang.lang_system['recovering'], option_2=lang.lang_system['exit'], option_3=lang.lang_system["continue session"])
        if msg.get() == lang.lang_system['exit']:
            sys.exit()
        elif msg.get() == lang.lang_system['recovering']:
            os.remove('cfg.py')
            shutil.copy('modules/cfg_backup.py', 'cfg_backup.py')
            os.rename('cfg_backup.py', 'cfg.py')
            CTkMessagebox(title='Settings', message=lang.lang_system['restart musplayer 2'])
    except:
        pass


def setting():

    def on_closing():
        if error_situs == True:
            sys.exit()
        elif error_situs == False:
            des.destroy()

    #function for equoliser
    def sequency_event(value):
        global sequency
        sequency = value
        fq = lang.lang_system['freq']
        text_seque.configure(text = f'{fq}: {int(value)} Hz')
    def buffer_event(choise):
        global buffer
        buffer = choise
        br = lang.lang_system['buffer']
        text_buff.configure(text = f'{br}: {int(choise)} KB')
    def bits_event(bit_choise):
        global bit
        bit = bit_choise
        bt = lang.lang_system['bits']
        text_bits.configure(text = f'{bt}: {int(bit_choise)} Bit')
    def sound_mode_event(soundchoise):
        global sound
        if soundchoise =='mono':
            sound = 1
        elif soundchoise == 'stereo':
            sound = 2
        smd = lang.lang_system['sound mode']
        text_sound_mode.configure(text = f'{smd}: {soundchoise}')
    def apply_equoliser():
        muciser.custom_init(int(sequency), int(buffer), int(bit), int(sound))
        MainAPI.stop()

    #function for customisation
    def change_dir_theme():
        global theme_dir
        theme_dir = filedialog.askdirectory(title='Change theme dir')
        path_theme_entry.delete(first_index=0, last_index = END)
        path_theme_entry.insert(index = 0, string = theme_dir)
    def change_dir_theme_tray():
        global theme_dir_tray
        theme_dir_tray = filedialog.askdirectory(title='Change theme dir')
        path_theme_tray_entry.delete(first_index=0, last_index = END)
        path_theme_tray_entry.insert(index = 0, string = theme_dir_tray)
    def apply_themes():
        if theme_dir == '':
            CTkMessagebox(title=lang.lang_system['settings'], message=lang.lang_system['no_changed path'])
        else:
            if theme_dir_tray == '':
                CTkMessagebox(title=lang.lang_system['settings'], message=lang.lang_system['no_changed path'])
        try:
            os.remove('cfg.py')
        except:
            pass
        theme_cfg = open('cfg.py', 'w+')
        theme_cfg.write(f"theme = '{os.path.basename(theme_dir)}'")
        theme_cfg.write(f"\ntheme_tray = '{os.path.basename(theme_dir_tray)}'")
        theme_cfg.write(f"\nlang = '{lang_var}'")
        theme_cfg.close()
        CTkMessagebox(title=lang.lang_system['settings'], message=lang.lang_system['restart musplayer 2'])

    #function for Download
    def changer_format(value):
        if value == 'audio':
            format_files_combo.configure(values=['.mp3', '.ogg', '.wav'])
        elif value == 'video':
            format_files_combo.configure(values=['.mp4', '.avi', '.webm'])
    def download_content():

        
        if type_file_combo.get() == 'audio':
            pass
        elif type_file_combo.get() == 'video':
            pass
        else:
            CTkMessagebox(title=lang.lang_system['download'], message=lang.lang_system['error'])

        if (format_files_combo.get() == '.mp3' or format_files_combo.get() == '.ogg' or format_files_combo.get() ==  '.wav'
        or format_files_combo.get() == '.avi' or format_files_combo.get() == '.webm' or format_files_combo.get() ==  '.mp4'):
            pass
        else:
            CTkMessagebox(title=lang.lang_system['download'], message=lang.lang_system['error'])

        if url_type.get() == 'internet URL':
            path_save_file = filedialog.askdirectory(title='Save file')

            dialog = CTkInputDialog(text=lang.lang_system['name_music'], title=lang.lang_system['name_music'])
            name_music = print(dialog.get_input())
            progressbar_download.configure(text=lang.lang_system['download'])
            des.update()

            try:
                wget.download(url = f'{url_entry.get()}', out = f'{path_save_file}/{name_music}{format_files_combo.get()}')
                CTkMessagebox(title=lang.lang_system['download'], message=lang.lang_system['done'])
                progressbar_download.configure(text = lang.lang_system['get start'])
            except:
                CTkMessagebox(title=lang.lang_system['download'], message=lang.lang_system['error'])      
        elif url_type.get() == 'Youtube URL':
            if type_file_combo.get() == 'audio':
                path_save_file = filedialog.askdirectory(title='Save file')
                progressbar_download.configure(text=lang.lang_system['download'])
                des.update()
                des.focus_force()

                try:
                    streams = YouTube(f'{url_entry.get()}')
                    old_name_sream = streams.title
                    streams = YouTube(f'{url_entry.get()}').streams
                    streams.filter(progressive=True).desc().first().download(output_path = f'{path_save_file}', filename=f'musicfile.mp4')
                    progressbar_download.configure(text = lang.lang_system['converting'])
                    des.update()
                    audioclip = AudioFileClip(f'{path_save_file}/musicfile.mp4')
                    audioclip.write_audiofile(filename = f'{path_save_file}/musicfile{format_files_combo.get()}')
                    os.remove(f'{path_save_file}/musicfile.mp4')

                    progressbar_download.configure(text = lang.lang_system['get start'])
                    donemusic= lang.lang_system['done music']
                    CTkMessagebox(title=lang.lang_system['download'], message=f'{donemusic}{format_files_combo.get()})')
                except:
                    progressbar_download.configure(text = lang.lang_system['get start'])
                    CTkMessagebox(title=lang.lang_system['download'], message=lang.lang_system['error'])

                

            elif type_file_combo.get() == 'video':
                path_save_file = filedialog.askdirectory(title='Save file')
                progressbar_download.configure(text=lang.lang_system['download'])
                des.update()
                des.focus_force()

                try:
                    streams = YouTube(f'{url_entry.get()}')
                    name_sream = streams.title
                    streams = YouTube(f'{url_entry.get()}').streams
                    streams.filter(progressive=True).desc().first().download(f'{path_save_file}', filename=f'musicfile.mp4')
                    if format_files_combo.get() == '.mp4':
                        pass
                    else:
                        progressbar_download.configure(text = 'Converting file. Please wait...')
                        des.update()
                        audioclip = VideoFileClip(f'{path_save_file}/musicfile.mp4')
                        audioclip.write_videofile(filename = f'{path_save_file}/musicfile{format_files_combo.get()}', fps = 10)
                        os.remove(f'{path_save_file}/musicfile.mp4')

                    progressbar_download.configure(text = lang.lang_system['get start'])
                    donemusic= lang.lang_system['done music']
                    CTkMessagebox(title=lang.lang_system['download'], message=f'{donemusic}{format_files_combo.get()})')
                except:
                    progressbar_download.configure(text = lang.lang_system['get start'])
                    CTkMessagebox(title='Download', message='Error')

            else:
                CTkMessagebox(title=lang.lang_system['download'], message=lang.lang_system['error'])
        else:
            CTkMessagebox(title=lang.lang_system['download'], message=lang.lang_system['error'])

    #Function for Localisation
    def change_language(value):
        global lang_var
        lang_var = value
    def apply_language():
        try:
            os.remove('cfg.py')
        except:
            pass
        theme_cfg = open('cfg.py', 'w+')
        theme_cfg.write(f"theme = '{os.path.basename(theme_dir)}'")
        theme_cfg.write(f"\ntheme_tray = '{os.path.basename(theme_dir_tray)}'")
        theme_cfg.write(f"\nlang = '{lang_var}'")
        theme_cfg.close()
        CTkMessagebox(title=lang.lang_system['settings'], message=lang.lang_system['restart musplayer 2'])

    #update
    def update_prover():
         up = updater.update(vers)
         if up == 'present':
             CTkMessagebox(title=lang.lang_system['settings'], message=lang.lang_system['present'])
         elif up == 'new':
             upds = CTkMessagebox(title=lang.lang_system['settings'], message=lang.lang_system['update musplayer 2'], option_1=lang.lang_system['update'], option_2=lang.lang_system['continue session'])
             if upds.get(lang.lang_system['update']):
                 pass


    def equolizing():
        text_header_settings.configure(text=lang.lang_system['equoliz'])
        text_seque.place(x=250, y= 80)
        seque.place(x=250,y=110)
        text_buff.place(x=250, y=150)
        buff.place(x=250, y=180)
        text_bits.place(x=250, y=220)
        bits.place(x=250, y=250)
        text_sound_mode.place(x=250, y = 290)
        sound_mode.place(x = 250, y = 320)
        apply_equo.place(x = 550, y = 350)


        path_theme_label.place_forget()
        path_theme_entry.place_forget()
        path_theme_button.place_forget()
        path_theme_tray_label.place_forget()
        path_theme_tray_button.place_forget()
        path_theme_tray_entry.place_forget()
        path_theme_apply_button.place_forget()

        music_label.place_forget()
        url_type.place_forget()
        change_audio_video_label.place_forget()
        type_file_combo.place_forget()
        format_files_combo.place_forget()
        get_url_address.place_forget()
        url_entry.place_forget()
        download_button.place_forget()
        progressbar_download.place_forget()

        label_lang.place_forget()
        lang_type.place_forget()
        apply_lang.place_forget()

        image_version.place_forget()
        text_version.place_forget()
        update_version.place_forget()


    def customizing():
        text_header_settings.configure(text=lang.lang_system['customiz'])


        music_label.place_forget()
        url_type.place_forget()
        change_audio_video_label.place_forget()
        type_file_combo.place_forget()
        format_files_combo.place_forget()
        get_url_address.place_forget()
        url_entry.place_forget()
        download_button.place_forget()
        progressbar_download.place_forget()

        path_theme_label.place(x=250, y=80)
        path_theme_entry.place(x=250, y=110)
        path_theme_button.place(x=510, y = 110)
        path_theme_tray_label.place(x=250, y=150)
        path_theme_tray_entry.place(x=250, y=180)
        path_theme_tray_button.place(x=510, y=180)
        path_theme_apply_button.place(x = 550, y = 350)

        apply_equo.place_forget()
        sound_mode.place_forget()
        text_sound_mode.place_forget()
        bits.place_forget()
        text_bits.place_forget()
        buff.place_forget()
        text_buff.place_forget()
        seque.place_forget()
        text_seque.place_forget()

        label_lang.place_forget()
        lang_type.place_forget()
        apply_lang.place_forget()

        image_version.place_forget()
        text_version.place_forget()
        update_version.place_forget()

    def downloazing():
        text_header_settings.configure(text=lang.lang_system['downloadiz'])

        music_label.place(x=250, y=80)
        url_type.place(x = 250, y=110)
        change_audio_video_label.place(x=250,y=145)
        type_file_combo.place(x=250, y=180)
        format_files_combo.place(x=510, y=180)
        get_url_address.place(x=250, y=210)
        url_entry.place(x=250, y=240)
        download_button.place(x = 550, y = 350)
        progressbar_download.place(x=250,y = 280)

        apply_equo.place_forget()
        sound_mode.place_forget()
        text_sound_mode.place_forget()
        bits.place_forget()
        text_bits.place_forget()
        buff.place_forget()
        text_buff.place_forget()
        seque.place_forget()
        text_seque.place_forget()

        path_theme_label.place_forget()
        path_theme_entry.place_forget()
        path_theme_button.place_forget()
        path_theme_tray_label.place_forget()
        path_theme_tray_button.place_forget()
        path_theme_tray_entry.place_forget()
        path_theme_apply_button.place_forget()

        label_lang.place_forget()
        lang_type.place_forget()
        apply_lang.place_forget()

        image_version.place_forget()
        text_version.place_forget()
        update_version.place_forget()

    def localiz():
        text_header_settings.configure(text=lang.lang_system['localiz'])

        label_lang.place(x=250, y=80)
        lang_type.place(x = 250, y=110)
        apply_lang.place(x = 550, y = 350)

        apply_equo.place_forget()
        sound_mode.place_forget()
        text_sound_mode.place_forget()
        bits.place_forget()
        text_bits.place_forget()
        buff.place_forget()
        text_buff.place_forget()
        seque.place_forget()
        text_seque.place_forget()

        path_theme_label.place_forget()
        path_theme_entry.place_forget()
        path_theme_button.place_forget()
        path_theme_tray_label.place_forget()
        path_theme_tray_button.place_forget()
        path_theme_tray_entry.place_forget()
        path_theme_apply_button.place_forget()

        music_label.place_forget()
        url_type.place_forget()
        change_audio_video_label.place_forget()
        type_file_combo.place_forget()
        format_files_combo.place_forget()
        get_url_address.place_forget()
        url_entry.place_forget()
        download_button.place_forget()
        progressbar_download.place_forget()

        image_version.place_forget()
        text_version.place_forget()
        update_version.place_forget()

    def updating():
        text_header_settings.configure(text=lang.lang_system['update'])

        image_version.place(x=250, y=80)
        text_version.place(x = 380, y=80)
        update_version.place(x = 380, y = 140)        

        apply_equo.place_forget()
        sound_mode.place_forget()
        text_sound_mode.place_forget()
        bits.place_forget()
        text_bits.place_forget()
        buff.place_forget()
        text_buff.place_forget()
        seque.place_forget()
        text_seque.place_forget()

        path_theme_label.place_forget()
        path_theme_entry.place_forget()
        path_theme_button.place_forget()
        path_theme_tray_label.place_forget()
        path_theme_tray_button.place_forget()
        path_theme_tray_entry.place_forget()
        path_theme_apply_button.place_forget()

        music_label.place_forget()
        url_type.place_forget()
        change_audio_video_label.place_forget()
        type_file_combo.place_forget()
        format_files_combo.place_forget()
        get_url_address.place_forget()
        url_entry.place_forget()
        download_button.place_forget()
        progressbar_download.place_forget()

        label_lang.place_forget()
        lang_type.place_forget()
        apply_lang.place_forget()



    des = CTkToplevel()
    des.geometry('700x400')
    des.title(lang.lang_system['settings'])
    des.resizable(width=False, height=False)

    punktFrame = CTkScrollableFrame(des, width=210, height=360)
    punktFrame.place(x=10,y=10)

    text_header = CTkLabel(punktFrame, text=lang.lang_system['settings'], font=('Segoe UI Light', 20))
    text_header.pack()

    button_equo = CTkButton(punktFrame, text=lang.lang_system['equoliz'], command=equolizing)
    button_equo.pack(fill=X, pady=10)

    button_customiz = CTkButton(punktFrame, text=lang.lang_system['customiz'], command=customizing)
    button_customiz.pack(fill=X, pady=10)

    button_download = CTkButton(punktFrame, text=lang.lang_system['downloadiz'], command=downloazing)
    button_download.pack(fill=X, pady=10)

    button_localization = CTkButton(punktFrame, text=lang.lang_system['localiz'], command=localiz)
    button_localization.pack(fill=X, pady=10)

    button_update = CTkButton(punktFrame, text=lang.lang_system['update'], command=updating)
    button_update.pack(fill=X, pady=10)

    
    text_header_settings = CTkLabel(des, text=lang.lang_system['settings'], font=('Segoe UI', 30))
    text_header_settings.place(x=250, y=10)


    #Equoliser
    seque = CTkSlider(des, from_=0, to=44100, command=sequency_event)
    text_seque = CTkLabel(des, text=lang.lang_system['settings'])
    buff = CTkComboBox(des, values=["512", "1024", "2048", "4096"], variable='', state='readonly', command=buffer_event)
    text_buff = CTkLabel(des, text=lang.lang_system['buffer'])
    bits = CTkComboBox(des, values=["8", "16", "32"], state='readonly', variable='', command=bits_event)
    text_bits = CTkLabel(des, text=lang.lang_system['bits'])
    sound_mode = CTkComboBox(des, values=["mono", 'stereo'], state='readonly', variable='', command=sound_mode_event)
    text_sound_mode = CTkLabel(des, text=lang.lang_system['sound mode'])
    apply_equo = CTkButton(des, text = lang.lang_system['apply'],  command=apply_equoliser)

    #Customisation
    path_theme_label = CTkLabel(des, text=lang.lang_system['ui path'] )
    path_theme_entry = CTkEntry(des, placeholder_text='path', width = 250)
    path_theme_button = CTkButton(des, text=lang.lang_system['change'], width = 100, command=change_dir_theme)
    path_theme_tray_label = CTkLabel(des, text=lang.lang_system['tray path'])
    path_theme_tray_entry = CTkEntry(des, placeholder_text='path',width = 250)    
    path_theme_tray_button = CTkButton(des, text=lang.lang_system['change'], width = 100, command=change_dir_theme_tray)
    path_theme_apply_button = CTkButton(des, text=lang.lang_system['apply'], command=apply_themes)

    #Download
    format_files_combo = CTkComboBox(des, state='readonly', variable='change video or audio filetype')
    type_file_combo = CTkComboBox(des, values=['video', 'audio'], width=250, state='readonly', command=changer_format)
    url_type = CTkComboBox(des, values=['internet URL', 'Youtube URL'], state='readonly', width=400)
    url_entry = CTkEntry(des, placeholder_text=lang.lang_system['get url'], width=400)
    download_button = CTkButton(des, text=lang.lang_system['download'], command=download_content)
    music_label = CTkLabel(des, text = lang.lang_system['type url'])
    change_audio_video_label = CTkLabel(des, text=lang.lang_system['change format'])
    get_url_address = CTkLabel(des, text = lang.lang_system['get url'])
    progressbar_download = CTkLabel(des, text = lang.lang_system['get start'])

    #Localisation
    lang_type = CTkComboBox(des, state='readonly', values=['en', 'ru'], command=change_language)
    label_lang = CTkLabel(des, text=lang.lang_system['change lang'])
    apply_lang = CTkButton(des, text=lang.lang_system['apply'], command=apply_language)

    #update
    update_version = CTkButton(des, text = lang.lang_system['update'], command = update_prover)
    text_version = CTkLabel(des, text = f'musplayer 2 {vers} "Bibs beta"')
    update_image = imager.imagefile('src/ui/update.png')
    image_version = CTkLabel(des, text = '', image=update_image)

    des.protocol("WM_DELETE_WINDOW", on_closing)
    des.mainloop()

#setting()
