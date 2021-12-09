import numpy
import time
# Merge sort O(n log n)
# Separetes array in halfs until they are of size 1. O(log n)
# Then compares values in halfs to eachother and merges them in a sorted order O(n)
# 
#
#
#
def isSorted(a):
    n = len(a)
    return all(a[i] <= a[i+1] for i in range(n-1))

def mergeSort(array):
    if len(array) == 1:
        return

    middle = len(array)//2
    leftHalf = array[:middle]
    rightHalf = array[middle:]
    mergeSort(leftHalf)
    mergeSort(rightHalf)

    indexL, indexR, indexA = 0, 0, 0

    while indexL < len(leftHalf) and indexR < len(rightHalf):
        if leftHalf[indexL] < rightHalf[indexR]:
            array[indexA] = leftHalf[indexL]
            indexL += 1
        else:
            array[indexA] = rightHalf[indexR]
            indexR += 1
        indexA +=1

    while indexL < len(leftHalf):
        array[indexA] = leftHalf[indexL]
        indexL += 1
        indexA += 1    

    while indexR < len(rightHalf):
        array[indexA] = rightHalf[indexR]
        indexR += 1
        indexA += 1 


if __name__ == "__main__" :
    timer = time.time()
    aArray = numpy.random.randint(10000,size=5000)
    timer = time.time()
    mergeSort(aArray)
    print("--- %s seconds ---" % (time.time() - timer))
    if isSorted(aArray): print("Array is sorted")