import os
from tkinter import filedialog
import time
import wget
import shutil

lang_proc = True
choose_os_in = ''
bits = ''

while lang_proc:
    lang_in = input('Choose language/Выберите язык\nRu/En: ')
    if lang_in == 'Ru' or lang_in == 'En' or lang_in == 'ru' or lang_in == 'en':
        lang_proc = False


if lang_in == 'Ru' or lang_in == 'ru' :
    lang = {
    'welcome': 'Добро пожаловать в BuildMas - сборчик программы musplayer 2',
    'choose os': 'Выберите операционную систему: Windows 7, Windows 8.1, Windows 10: ',
    'choose bits': 'Выберите разрядность: x86 или x64: ', 
    'work dir': 'Выберите папку для дальнейших операций',
    '1step': 'Скачивание интерпретатора, исходники musplayer 2',
    '2step': 'Распаковка интерпретатора, настройка переменной path',
    '3step': 'Скачивание модулей для сборки',
    '4step': 'Скачивание сборочного конфига',
    '5step': 'Сборка программы',
    '6step': 'Архивация программы и перемещение в рабочую папку',
    '7step': "Очистка переменной path",
    '8step': 'Удаление модулей, исходники, интерпретатора',
    '9step': 'Завершение'
    }
elif lang_in == 'En' or lang_in == 'en' :
    lang = {
    'welcome': 'Welcome to BuildMas -o builder program musplayer 2',
    'choose os': 'Choose Operating System: Windows 7, Windows 8.1, Windows 10, Windows 11: ',
    'choose bits': 'Choose bits: x86 or x64: ',
    'work dir': 'Choose work path for next operation','1step': 'Скачивание интерпретатора, исходники musplayer 2',
    '1step': 'Downloading interpretier, source muspalyer 2',
    '2step': 'Unpack archive, setting variable path',
    '3step': 'Downloading modules for build',
    '4step': 'Downloading a bild config',
    '5step': 'Building program',
    '6step': 'Archiving program and replacing in the work path',
    '7step': "Clean variable path",
    '8step': 'Deleting modules, sources, interpretier',
    '9step': 'Ending'
    }

print(lang['welcome'])

chooseos = True

while chooseos:
    choose_os_in = input(lang['choose os'])
    if choose_os_in=='Windows 7' or choose_os_in=='windows 7' or choose_os_in=='Windows 8.1' or choose_os_in=='windows 8.1' or choose_os_in=='Windows 10' or choose_os_in=='windows 10' or choose_os_in=='Windows 11' or choose_os_in=='windows 11':
        chooseos = False

choosebits = True

while choosebits:
    if choose_os_in == 'Windows 11' or choose_os_in == 'windows 11':
        bits = 'x64'
        choosebits = False
    else:
        bits = input(lang['choose bits'])
        if bits == 'x86' or bits == 'x64':
            choosebits = False

if lang_in == 'Ru' or lang_in == 'ru' :
    choosed = {
    'you choosed': f'Вы выбрали {choose_os_in} с разрядностью {bits}'
    }
elif lang_in == 'En' or lang_in == 'en' :
    choosed ={ 
    'you choosed': f'You choosed {choose_os_in} with bits {bits}'
    }

print(choosed['you choosed'])

path = filedialog.askdirectory(title=lang['work dir'])

if lang_in == 'Ru' or lang_in == 'ru' :
    if path == '':
        raise NameError('вы не прописали папку')
    else:
        print(f'Вы выбрали {path}')
elif lang_in == 'En' or lang_in == 'en' :
    if path == '':
        raise NameError('You not printed path')
    else:
        print(f'You choosed {path}')

print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print(0)

os.chdir(path=path)

print(lang['1step'])

if choose_os_in == 'Windows 7' or 'windows 7':
    if bits == 'x86':
        wget.download('https://www.python.org/ftp/python/3.8.9/python-3.8.9-embed-win32.zip')
    elif bits == 'x64':
        wget.download('https://www.python.org/ftp/python/3.8.9/python-3.8.9-embed-amd64.zip')