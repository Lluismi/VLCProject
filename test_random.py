from logica import listaidcanciones
from logica import listaleatoria
from logica import randompath

def test_listrandomid():
    assert len(listaleatoria())== len(listaidcanciones())

def test_norepeat():
    listanorepeat = listaleatoria()
    for id in listanorepeat:
        if listanorepeat.count(id) > 1:
            assert False
    assert True

def test_asignaciónvalor():
    assert isinstance(randompath()[0], str)
    
