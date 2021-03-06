import Portafolio1;
import pytest;

def test_divisores_1():
    assert portafolio1.divisores(24) == '24, 12, 8, 6, 4, 3, 2, 1'
      
###########################################################################

def test_potenciaRecusivo_1():
    assert portafolio1.potenciaRecusivo(5, 2) == 25
    
###########################################################################    

def test_divisionRecusivo_1():
    assert portafolio1.divisionRecusivo(25, 5) == 5
    
def test_divisionRecusivo_2():
    assert isinstance(portafolio1.divisionRecusivo(25, 0), str) == isinstance('Error: División entre cero', str)
    
###########################################################################    

def test_corrimientoAEntero_1():
    assert portafolio1.corrimientoAEntero(133.5) == 1335
    
def test_corrimientoAEntero_2():
    assert portafolio1.corrimientoAEntero(-133.5) == -1335    
    
###########################################################################    

def test_contarDigitosFlotante_1():
    assert portafolio1.contarDigitosFlotante(133.578) == 6
    
def test_contarDigitosFlotante_2():
    assert portafolio1.contarDigitosFlotante(-133.578) == 6    
    
###########################################################################    

def test_indiceNumero_1():
    assert portafolio1.indiceNumero(1335, 3) == 5
    
def test_indiceNumero_2():
    assert isinstance(portafolio1.indiceNumero(1335, 8), str) == isinstance('Error: Indice fuera del rango del número', str)
    
###########################################################################    

def test_cortarNumero_1():
    assert portafolio1.cortarNumero(1335, 1, 2) == 33

def test_cortarNumero_2():
    assert isinstance(portafolio1.cortarNumero(1335, 8, 2), str) == isinstance('Error: Indices fuera del rango del número', str)  
