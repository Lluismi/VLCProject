import random
import xml.etree.ElementTree as ET
tree = ET.parse('Library.xml')
root = tree.getroot()


for track in root.iter('track'):
    songs = []
    songs.append()