import random
import xml.etree.ElementTree as ET
tree = ET.parse('Library.xml')
root = tree.getroot()

for child in root:
    songs = child.tag('canciones') 
    print (child.tag, child.attrib)
