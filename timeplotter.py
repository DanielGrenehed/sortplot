import matplotlib.pyplot as plt
from bubblesort import BubbleSort
from quicksort import QuickSort
from mergesort import mergeSort
from almostsort import almostSorted
import time
import random
import sys

def timeSort(array, sortFunc):
    start = time.time()
    if sortFunc == None:
        array.sort
    else:
        sortFunc(array)
    end = time.time()
    return end-start

def plotSort(sortFunc=None, funcName="DefaultSort"):
    random.seed(1337)
    array = []

    rtime= []
    stime= []
    rstime= []
    atime= []
    nel = []
    n = 10
    while n < 100000:
        array = [random.randint(0, 100000) for _ in range(n)]
        print(f"Sorting {len(array)} elements with {funcName}")  
        rtime.append(timeSort(array.copy(), sortFunc))
        array.sort()
        stime.append(timeSort(array, sortFunc))
        almostSorted(array)
        atime.append(timeSort(array, sortFunc))
        array.reverse()
        rstime.append(timeSort(array.copy(), sortFunc))
        nel.append(n)
        n*=10
    plt.close()
    plt.plot(nel, rtime, label="unsorted")
    plt.plot(nel, stime, label="sorted")
    plt.plot(nel, rstime, label="reversed")
    plt.plot(nel, atime, label="almost")
    #plt.plot(nel, atime, label="almost")
    plt.xlabel("Array Size")
    plt.ylabel("Time")
    plt.title(funcName)
    plt.legend()
    plt.savefig(funcName+".png")
    plt.close()

if __name__ == "__main__" :
    sys.setrecursionlimit(1000000)
    plotSort(QuickSort, "QuickSort")
    plotSort(mergeSort, "MergeSort")
    plotSort(BubbleSort, "BubbleSort")
    plotSort()