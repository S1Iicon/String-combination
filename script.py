"""

In this script let's try to form all possible combinations with a chars
in string, for this problem I use the cartesian product with list in python.

"""

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