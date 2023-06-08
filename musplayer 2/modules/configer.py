from customtkinter import get_appearance_mode, set_appearance_mode

width_window = 740
height_window = 350

#set_appearance_mode('Light')

def get_config_info():
    return [width_window, height_window]

def apperiance():
    colormode = get_appearance_mode()

    if colormode == "Dark":
        colormode = 'black'
    elif colormode == 'Light':
        colormode = 'white'
    return colormode
