import random
from accesodatos import listaidcanciones


listaid = listaidcanciones()

def listaleatoria():
    songaleatorio = []
    for _ in range(len(listaid)):
        numero = random.choice(listaid)
        songaleatorio.append(numero)
        listaid.remove(numero)
    return songaleatorio