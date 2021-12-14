from timsort import TimSort
from mergesort import mergeSort
from heapsort import HeapSort
from almostsort import almostSorted
from perfdata import PerformaceData
from plotter import PlotPerfs
import random
import sys

def CreatePerformanceData():
    perfs = []
    perfs.append(PerformaceData(None, "DefaultSort"))
    perfs.append(PerformaceData(HeapSort, "HeapSort"))
    perfs.append(PerformaceData(mergeSort, "MergeSort"))
    perfs.append(PerformaceData(TimSort, "TimSort"))
    return perfs

def EnrichPerformanceData(perfs, start, end):
    n = start
    while n <= end:
        print(f"Testing with {n} elements")
        for d in perfs: 
            d.enrichElementCount(n)
        
        array = [random.randint(0, 100000) for _ in range(n)]
        for d in perfs: 
            d.enrichUnsorted(array.copy())

        array.sort()
        for d in perfs: 
            d.enrichSorted(array.copy())

        array.reverse()
        for d in perfs: 
            d.enrichReversed(array.copy())

        array = almostSorted(array)
        for d in perfs: 
            d.enrichAlmostSorted(array.copy())

        
        n*=2
    return perfs


if __name__ == "__main__" :
    sys.setrecursionlimit(1000000)
    if len(sys.argv) > 2:
        try:
            start = int(sys.argv[1])
            end = int(sys.argv[2])
            perfs = CreatePerformanceData()
            perfs = EnrichPerformanceData(perfs, pow(2, start), pow(2, end))
            PlotPerfs(perfs)
        except :
            print("Invalid arguments")
    else:
        perfs = CreatePerformanceData()
        perfs = EnrichPerformanceData(perfs, pow(2, 13), pow(2, 24))
        PlotPerfs(perfs)