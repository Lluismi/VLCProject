def tracks(id):
    count = 0
    for e in U:
        if e[0] == 'U':
            count = count + 1
    return count
print (measure_udacity(['Dave','Sebastian','Umika','Umberto']))

    for line in os.popen('cat' + os.environ["PWD"] + '/script.py') 

    


        
    songs = child.attrib(track) 
    print (child.tag, child.attrib)


    def parser(library):
        tree = ET.parse(library)
    root = tree.getroot()
    tracksDic = {}

    for library in root.iter("library"):
        for tracks in library:
            for track in tracks.findall("track"):
                tracksDic[track.attrib['ruta']] = track.attrib['id']
    return tracksDic