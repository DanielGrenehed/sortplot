import matplotlib.pyplot as plt
from timsort import TimSort
from mergesort import mergeSort
from heapsort import HeapSort
from almostsort import almostSorted
import random
import sys
import timeit

def timeSort(array, sortFunc):
    start = timeit.default_timer()
    if sortFunc == None:
        array.sort()
    else:
        sortFunc(array)
    end = timeit.default_timer()
    return end-start

def plotSort(sortFunc=None, funcName="DefaultSort"):
    random.seed(1337)
    array = []

    unsorted_time= []
    sorted_time= []
    reversed_time= []
    almost_time= []
    nel = []
    n = 1024 * 8
    while n <= 1048576 * 16:
        array = [random.randint(0, 100000) for _ in range(n)]
        print(f"Sorting {len(array)} elements with {funcName}")  
        unsorted_time.append(timeSort(array.copy(), sortFunc))
        array.sort()
        print("Sorted list")
        sorted_time.append(timeSort(array.copy(), sortFunc))
        almostSorted(array)
        print("Almost sorted list")
        almost_time.append(timeSort(array.copy(), sortFunc))
        array.sort()
        array.reverse()
        print("Reverse sorted list")
        reversed_time.append(timeSort(array.copy(), sortFunc))
        nel.append(n)
        n*=2
    print(unsorted_time)
    print(sorted_time)
    print(reversed_time)
    print(almost_time)

    plt.plot(nel, unsorted_time, label="unsorted", marker="o")
    plt.plot(nel, sorted_time, label="sorted", marker="o")
    plt.plot(nel, reversed_time, label="reversed", marker="o")
    plt.plot(nel, almost_time, label="almost", marker="o")
    plt.xscale('log', base=2)
    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.title(funcName)
    plt.legend()
    plt.savefig("graphs/"+funcName+".png")
    plt.close()
    return unsorted_time, nel

if __name__ == "__main__" :
    sys.setrecursionlimit(1000000)
    hs, nel = plotSort(HeapSort, "HeapSort")
    ms, nel = plotSort(mergeSort, "MergeSort")
    ts, nel = plotSort(TimSort, "TimSort")
    ds, nel = plotSort()

    plt.plot(nel, hs, label="HeapSort", marker="o")
    plt.plot(nel, ms, label="MergeSort", marker="o")
    plt.plot(nel, ts, label="TimSort", marker="o")
    plt.plot(nel, ds, label="DefaultSort", marker="o")
    plt.xscale('log', base=2)

    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.title("Sort-time for unsorted array")
    plt.legend()
    plt.savefig("graphs/comparison.png")
    plt.close()
    