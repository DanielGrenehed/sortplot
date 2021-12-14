"""
    HeapSort
    Worst-case      O(n log n)
    Best-case       O(n log n)
    Averaged-case   O(n log n)

"""


def Heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[l] > array[largest]:
        largest = l
    if r < n and array[r] > array[largest]:
        largest = r
    if largest != i :
        array[i], array[largest] = array[largest], array[i]
        Heapify(array, n, largest)

def HeapSort(array):
    n = len(array)
    for i in range(int(n/2)-1, -1, -1):
        Heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        Heapify(array, i, 0)

if __name__ == "__main__" :
    list = [2, 43 , 40, 3, 41, 50, 61, 31, 410, 1337, 1, -30, -324, 414, 13, -15]
    HeapSort(list)
    print(list)