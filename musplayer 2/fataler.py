import shutil
import os
from CTkMessagebox import CTkMessagebox

shutil.copy('modules/cfg_backup.py', 'cfg_backup.py')
os.rename('cfg_backup.py', 'cfg.py')
CTkMessagebox(title='Settings', message='Please restart musplayer 2')