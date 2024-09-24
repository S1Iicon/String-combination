"""

En este script vamos a tratar de formar todas las combinaciones
de un string, atendiendo a permutaciones y sin supresión de carácteres.

"""

# v1.0
# La solución de la cantidad de combinaciones (con permutación) aparentemente sería
# n!/(n - k)! Siendo "n" el número de letras y "k" el número de iteración.

def cartesian_product(string: str):
    string_list = [i for i in string]
    recollection = list()
    recollection.append(string_list)
    
    for i in range(len(string) - 1):
        image = list()
        for j in string_list:
            n = len(recollection) - 1
            for k in recollection[n]:
                if j not in k:
                    image += [j + k]
        recollection.append(image)
    return(recollection)