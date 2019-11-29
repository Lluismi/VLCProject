import random
from accesodatos import listaidcanciones
from accesodatos import rutacancionesid


def listaleatoria():
    listaid = listaidcanciones()
    songaleatorio = []
    for _ in range(len(listaid)):
        numero = random.choice(listaid)
        songaleatorio.append(numero)
        listaid.remove(numero)
    return songaleatorio


def randompath():
    listapathid = listaleatoria()
    path = []
    for id in listapathid:
        path.append(rutacancionesid[id])
    return path