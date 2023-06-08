echo "You must Installed"
echo "Python 3.10.9"
echo "Modules for Python:"
echo "nuitka"
echo "customtkinter"
echo "CTkMessageBox"
echo "pytaglib"
echo "pygame"
echo "moviepy"
timeout /t 3

python -m nuitka --windows-disable-console --follow-imports --windows-icon-from-ico=icon_black.ico start.py
