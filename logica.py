import random
from accesodatos import listaidcanciones


def listaleatoria(listaidcanciones):
    listaid = listaidcanciones()
    songaleatorio = []
    for _ in range(len(listaid)):
        numero = random.choice(listaid)
        songaleatorio.append(numero)
        listaid.remove(numero)
    return songaleatorio
print(listaleatoria(listaidcanciones))