import os
import subprocess
from subprocess import Popen
from accesodatos import pathcanciones
from logica import listaleatoria
    

def listapath():
    path = pathcanciones()
    rutavlc = "".join(path)
    vlc = "C:/Program Files/VideoLAN/VLC/vlc.exe"
    subprocess.Popen([vlc, [rutavlc]])
print(listapath())