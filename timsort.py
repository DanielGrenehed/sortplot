""" 
    TimSort
    Worst-case      O(n log n)
    Best-case       O(n)
    Average-case    O(n log n)
"""

MIN_MERGE = 64

def calcMinRun(n):
    r=0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n+r

def insertionSort(array, l, r):
    for i in range(l+1, r+1):
        j= i
        while j > l and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j-=1

def merge(array, start, mid, end):
    left_len, right_len = mid - start +1, end-mid
    left, right = [], []
    for i in range(0, left_len):
        left.append(array[start+i])
    for i in range(0, right_len):
        right.append(array[mid+1+i])
    
    i, j, k = 0,0,start

    while i < left_len and j < right_len:
        if left[i] <= right[j]:
            array[k] = left[i]
            i+=1
        else:
            array[k] = right[j]
            j+=1
        k+=1
    while i < left_len:
        array[k] = left[i]
        k+=1
        i+=1

def TimSort(array):
    n = len(array)
    blocksize = calcMinRun(n)

    for start in range(0, n, blocksize):
        end = min(start + blocksize -1, n-1)
        insertionSort(array, start, end)

    size = blocksize
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n-1, left+size-1)
            right = min((left+2*size-1), n-1)

            if mid < right:
                merge(array, left, mid, right)
        size*=2

if __name__ == "__main__" :
    list = [2, 43 , 40, 3, 41, 50, 61, 31, 410, 1337, 1, -30, -324, 414, 13, -15]
    TimSort(list)
    print(list)