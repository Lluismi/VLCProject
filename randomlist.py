<<<<<<< HEAD
import xml.etree.ElementTree as ET 

tree = ET.parse('Library.xml')
root = tree.getroot()

def lista(root):
    song = []
    for track in root.iter('track'):
        song.append(track.attrib)
print(lista)
=======
import random
import xml.etree.ElementTree as ET
tree = ET.parse('Library.xml')
root = tree.getroot()


for track in root.iter('track'):
    songs = []
    songs.append()
>>>>>>> 58323d737e8c37545dfe3d2d2cad038716a6bc9a
