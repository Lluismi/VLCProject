import os
import subprocess
from subprocess import Popen
from logica import randompath


def main():
    try:
        "C:/Program Files/VideoLAN/VLC/vlc.exe"
    except FileNotFoundError:
        print("No se ha encontrado el vlc.exe en la ruta indicada")
    vlc = "C:/Program Files/VideoLAN/VLC/vlc.exe"
    path = randompath()
    rutavlc = " ".join(path)
    subprocess.Popen([vlc, [rutavlc]])
