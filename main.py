import os
import subprocess
from subprocess import Popen
from logica import randompath


def main():
    path = randompath()
    rutavlc = " ".join(path)
    vlc = "C:/Program Files/VideoLAN/VLC/vlc.exe"
    subprocess.Popen([vlc, [rutavlc]])

if __name__ == "__main__":
    main()
