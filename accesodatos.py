import xml.etree.ElementTree as ET 


def listaidcanciones():
        tree = ET.parse('Library.xml')
        root = tree.getroot()
        idsong = []
        for track in root.find('cancions'):
                for id in track.findall('id'):
                        idsong.append(id.text)
        return idsong
print(listaidcanciones()) 

def pathcanciones():
        tree = ET.parse('Library.xml')
        root = tree.getroot()
        pathsong = []
        for track in root.find('cancions'):
                for path in track.findall('path'):
                        pathsong.append(path.text)
        return pathsong
print(pathcanciones())