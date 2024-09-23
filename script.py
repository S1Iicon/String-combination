"""

En este script vamos a tratar de formar todas las combinaciones
de un string, atendiendo a permutaciones y sin supresión de carácteres.

"""

# v1.0
# La solución de la cantidad de combinaciones (con permutación) aparentemente sería
# n!/(n! - k) Siendo "n" el número de letras y "k" el número de iteración.

def factorial(x: int):
    for i in range(x-1,0,-1):
        x *= i
    return x

def super_mega_combinator(string: str):
    for i in range(len(string)):
        for j in range(len(string)):
