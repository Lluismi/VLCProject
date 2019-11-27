import xml.etree.ElementTree as ET 


def listaidcanciones():
        tree = ET.parse('Library.xml')
        root = tree.getroot()
        idsong = []
        for child in root.iter('id'):
                idsong.append(child.text)
        return idsong

def pathcanciones():
        tree = ET.parse('Library.xml')
        root = tree.getroot()
        pathsong = []
        for child in root.iter('path'):
                pathsong.append(child.text) 
        return pathsong
print(pathcanciones())