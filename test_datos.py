from accesodatos import listaidcanciones
from accesodatos import pathcanciones



def test_listaid():
    assert len(listaidcanciones()) == 50

def test_listapath():
    assert len(pathcanciones()) == 50
    
