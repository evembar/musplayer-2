try:
    import cfg
except:
    import fataler

try :
    cfg.lang
except:    
    lang_system = {
        'loading musplayer 2': 'Loading\nmusplayer 2',
        'music name': 'Music name',
        'artist name': 'Artist name',
        'its music time': "It's music\n time!",
        'theme error': 'Light theme is not supported. Please switch to Dark theme.',
        'program ask': 'Change program ask',
        'exit': 'Exit',
        'continue session': 'Continue session',
        'minimize tray': 'Minimize to tray mod',
        'repeat mode off': 'Repeat mode on',
        'repeat mode on' : 'Repeat mode off',
        'unknown': 'unknown',
        'wwindow': 400,

        'about': 'about musplayer 2',
        'make by': 'Make by',

        'vider title': 'Vider - musplayer 2 plugin for watching video',
        'its video time': 'Its video time!',
        'please wait': 'Please wait...',

        'settings': 'Settings',
        'equoliz': 'Equolizer',
        'customiz': 'Customisation',
        'downloadiz': 'Download',
        'localiz': 'Localisation',
        'update': 'Update',

        'freq': 'Frequency',
        'buffer': 'Buffer',
        'bits': 'Bits',
        'sound mode': 'Sound Mode',

        'ui path': 'Theme path for player and vider',
        'tray path': 'Theme path for tray mode',

        'type url': 'Change Type URL',
        'change format': 'Change format file and type file',
        'get url': 'Get to URL Address',
        'get start': 'Get start to download',
        'converting': 'Converting file',
        'download': 'Download',
        'apply':'Apply',
        'change': 'Change',
        'done': 'Done',
        'done music': 'Done (file - musicfile',
        'error': 'Error',
        'path_src_error': 'Error in path src/',
        'no_changed path': 'No changed path',
        'recovering': 'recovering configuration with backup files',
        'restart musplayer 2': 'Please restart musplayer 2',
        'name_music': 'Name music',

        'update musplayer 2': 'Update musplayer 2?',

        'present': 'The present version',

        'change lang': 'Change Language',
        'fatal': "Fatal error in configurations"

    }


try:    
    if cfg.lang == 'ru':
        lang_system = {
            #ui musplayer 2
            'loading musplayer 2': 'Загрузка\nmusplayer 2',
            'music name': 'Название музыки',
            'artist name': 'Имя исполнителя',
            'its music time': 'Время\n музыки!',
            'theme error': 'Данная тема не поддерживается.\nПожалуйста, переключите тему.',
            'program ask': 'Что вы хотите сделать?',
            'exit': 'Выйти',
            'continue session': 'Продолжить использование',
            'minimize tray': 'Минимизация плеера', 
            'repeat mode off': 'Повторения выключены',
            'repeat mode on' : 'Повторения включены',
            'unknown': 'Неизвестный',
            'wwindow': 500,

            'about': 'о musplayer 2',
            'make by': 'Разработал',

            'vider title': 'Vider - musplayer 2 плагин для просмотра видео',
            'its video time': 'Время видео!',
            'please wait': 'Пожалуйста подождите...',

            'settings': 'Настройки',
            'equoliz': 'Эквалайзер',
            'customiz': 'Кастомизация',
            'downloadiz': 'Скачать ',
            'localiz': 'Локализация',

            'update': 'Обновление',
            'freq': 'Частота',
            'buffer': 'Буфер',
            'bits': 'Разрядность',
            'sound mode': 'Режим воспроизведения',

            'ui path': 'Папка с темой кнопок для плеера и Vider',
            'tray path': 'Папка с темой кнопок для трея',

            'type url': 'Выберите тип URL',
            'change format': 'Выберите формат файла, а таже расширение',
            'get url': 'Впишите URL адрес',
            'get start': 'Нажмите "Скачать" для скачивания',
            'converting': 'Конвертирование файла',
            'download': 'Скачать',
            'apply':'Применить',
            'change': 'Выбрать',
            'done': 'Готово',
            'done music': 'Готово (файл - musicfile',
            'error': 'Ошибка',
            'path_src_error': 'Ошибка папки src/',
            'no_changed path': 'Не найдена папка',
            'recovering': 'Восстановить конфигурационный файл с бэкапа',
            'restart musplayer 2': 'Пожалуйста перезагрузите musplayer 2',
            'name_music': 'Имя музыки',

            'update musplayer 2': 'Обновить musplayer 2?',

            'present': 'В обновлении не нуждается',

            'change lang': 'Выберите язык',
            'fatal': "Фатальная ошибка в конфигурации"
        }
    elif cfg.lang == 'en':
        lang_system = {
            'loading musplayer 2': 'Loading\nmusplayer 2',
            'music name': 'Music name',
            'artist name': 'Artist name',
            'its music time': "It's music\n time!",
            'theme error': 'Light theme is not supported. Please switch to Dark theme.',
            'program ask': 'Change program ask',
            'exit': 'Exit',
            'continue session': 'Continue session',
            'minimize tray': 'Minimize to tray mod',
            'repeat mode off': 'Repeat mode on',
            'repeat mode on' : 'Repeat mode off',
            'unknown': 'unknown',
            'wwindow': 400,

            'about': 'about musplayer 2',
            'make by': 'Make by',

            'vider title': 'Vider - musplayer 2 plugin for watching video',
            'its video time': 'Its video time!',
            'please wait': 'Please wait...',

            'settings': 'Settings',
            'equoliz': 'Equolizer',
            'customiz': 'Customisation',
            'downloadiz': 'Download',
            'localiz': 'Localisation',
            'update': 'Update',

            'freq': 'Frequency',
            'buffer': 'Buffer',
            'bits': 'Bits',
            'sound mode': 'Sound Mode',

            'ui path': 'Theme path for player and vider',
            'tray path': 'Theme path for tray mode',
            
            'type url': 'Change Type URL',
            'change format': 'Change format file and type file',
            'get url': 'Get to URL Address',
            'get start': 'Get start to download',
            'converting': 'Converting file',
            'download': 'Download',
            'apply':'Apply',
            'change': 'Change',

            'done': 'Done',
            'done music': 'Done (file - musicfile',
            'error': 'Error',
            'path_src_error': 'Error in path src/',
            'no_changed path': 'No changed path',
            'recovering': 'recovering configuration with backup files',
            'restart musplayer 2': 'Please restart musplayer 2',
            'name_music': 'Name music',

            'update musplayer 2': 'Update musplayer 2?',

            'present': 'The present version',

            'change lang': 'Change Language',
            'fatal': "Fatal error in configurations"
        }
    else:
        lang_system = {
            'loading musplayer 2': 'Loading\nmusplayer 2',
            'music name': 'Music name',
            'artist name': 'Artist name',
            'its music time': "It's music\n time!",
            'theme error': 'Light theme is not supported. Please switch to Dark theme.',
            'program ask': 'Change program ask',
            'exit': 'Exit',
            'continue session': 'Continue session',
            'minimize tray': 'Minimize to tray mod',
            'repeat mode off': 'Repeat mode on',
            'repeat mode on' : 'Repeat mode off',
            'unknown': 'unknown',
            'wwindow': 400,

            'about': 'about musplayer 2',
            'make by': 'Make by',

            'vider title': 'Vider - musplayer 2 plugin for watching video',
            'its video time': 'Its video time!',
            'please wait': 'Please wait...',

            'settings': 'Settings',
            'equoliz': 'Equolizer',
            'customiz': 'Customisation',
            'downloadiz': 'Download',
            'localiz': 'Localisation',
            'update': 'Update',

            'freq': 'Frequency',
            'buffer': 'Buffer',
            'bits': 'Bits',
            'sound mode': 'Sound Mode',

            'ui path': 'Theme path for player and vider',
            'tray path': 'Theme path for tray mode',

            'type url': 'Change Type URL',
            'change format': 'Change format file and type file',
            'get url': 'Get to URL Address',
            'get start': 'Get start to download',
            'converting': 'Converting file',
            'download': 'Download',
            'apply':'Apply',
            'change': 'Change',

            'done': 'Done',
            'done music': 'Done (file - musicfile',
            'error': 'Error',
            'path_src_error': 'Error in path src/',
            'no_changed path': 'No changed path',
            'recovering': 'recovering configuration with backup files',
            'restart musplayer 2': 'Please restart musplayer 2',
            'name_music': 'Name music',

            'update musplayer 2': 'Update musplayer 2?',

            'present': 'The present version',

            'change lang': 'Change Language',
            'fatal': "Fatal error in configurations"
        }
except:
    pass