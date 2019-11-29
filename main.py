import os
import subprocess
from subprocess import Popen
from logica import randomskere


def listapath():
    path = randomskere()
    rutavlc = " ".join(path)
    vlc = "C:/Program Files/VideoLAN/VLC/vlc.exe"
    subprocess.Popen([vlc, [rutavlc]])


listapath()
