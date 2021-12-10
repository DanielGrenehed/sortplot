import random
import numpy

def almostSorted(array: list):
    if len(array) < 3:
        return array
    """    
    if len(array) == 3:
        array.sort()
        swap = random.randint(0,1)
        array[swap], array[swap + 1], = array[swap+1], array[swap]
        return array
    """
    array.sort()
    numberOfSwaps = len(array)//10 if len(array) >= 10 else 1
    indexes = random.sample(range(0, len(array)-2, 2), numberOfSwaps)
    for index in indexes:
        array[index], array[index+1] = array[index + 1], array[index]
    return array



