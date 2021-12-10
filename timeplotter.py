import matplotlib.pyplot as plt
from bubblesort import BubbleSort
from quicksort import QuickSort
from mergesort import mergeSort
import time
import random

def plotSort(sortFunc=None, funcName="DefaultSort"):
    random.seed(1337)
    print(random.random())
    array = []

    print(f"Sorting {len(array)} elements with {funcName}")     
    start = time.time()
    if sortFunc == None:
        array.sort
    else:
        sortFunc(array)
    ent = time.time()

    """
        sort unsorted
        sort sorted
        sort reversed sorted
        sort almost sorted

        plot order( time(y), array_size(x))
        Save to file (funcname.png)        
    """
    pass

if __name__ == "__main__" :
    plotSort(QuickSort, "QuickSort")
    plotSort(mergeSort, "MergeSort")
    plotSort(BubbleSort, "BubbleSort")
    plotSort()