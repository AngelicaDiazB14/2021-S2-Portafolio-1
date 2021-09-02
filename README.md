# 2021 S2 Portafolio #1

El archivo debe llamarse **Portafolio1.py**, además respetar el nombre de las funciones que más adelante se describen
Recordar hacer las validaciones de cada una de las restricciones

## divisores(num)
Imprimir los divisores de un número de manera descendente.
Solo números enteros positivos

```python
>>>divisores(24)
'24, 12, 8, 6, 4, 3, 2, 1'
```

## potenciaRecusivo(base, exponente)  
Potencia de un número base elevado a un número exponente sin utilizar el operador de potencia
Para ambos parámtros solo números enteros positivos

```python
>>>potenciaRecusivo(5, 2)
25
```

## divisionRecusivo(dividendo, divisor)
Resultado de la división entera un número “dividendo” entre un número “divisor” sin utilizar el operador de división
Para ambos parámtros solo números enteros positivos
Tomar en cuenta la divisón entre cero no es permitido

```python
>>>divisionRecusivo(25, 5)
5
```

## corrimientoAEntero(num)
Corrimientos al entero, pasar los números de la parte decimal a la parte entera. 
Mantener el signo en el caso que sea negativo

```python
>>>corrimientoAEntero(133.5)   
1335
```
## contarDigitosFlotante(num)
Devolver la cantidad de dígitos que tiene esta representación numérica, pero esta vez tomando en cuenta los dógitos de la parte de los decimales. El número puede ser positivos o negativos
```python
>>>contarDigitosFlotante(133.578)
6
```
## indiceNumero(num, indice)
Retorna el dígito del número según índices
Para ambos parámtros solo números enteros positivos
```python
>>>indiceNumero(1335, 3)  	
5
```
## cortarNumero(num, ini, fin)
Construir una función que reciba un número y ordenados de manera ascendente.
Para ambos parámtros solo números enteros positivos
Verificar que los parámtros ini y fin no sobre pasen el largo del número
```python
>>>cortarNumero(1335, 1, 2)
33
```

