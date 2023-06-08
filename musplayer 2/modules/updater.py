import wget
import os

def update(version):

    if os.path.isfile('musplayer 2.txt'):
        os.remove('musplayer 2.txt')
    else:
        pass


    wget.download('https://gitlab.com/lbhnik12/comine/-/raw/main/musplayer 2.txt?inline=false')
    vers = open('musplayer 2.txt', 'r+')
    vers_up = vers.read()
    if float(vers_up) > float(version):
        vers.close()
        os.remove('musplayer 2.txt')
        return 'new'
    elif float(vers_up) == float(version):
        vers.close()
        os.remove('musplayer 2.txt')
        return 'present'
