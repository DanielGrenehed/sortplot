

def partition(list, lo, hi):
    pivot = list[hi]
    i = lo-1
    for j in range(lo, hi):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    i+=1
    list[i], list[j] = list[j], list[i]
    return i

def QuickSort(list, lo=0, hi=None):
    if hi == None:
        hi = len(list)-1
    if lo >= hi or lo < 0:
        return
    p = partition(list, lo, hi)

    QuickSort(list, lo, p-1)
    QuickSort(list, p+1, hi)



if __name__ == "__main__" :
    list = [2, 43 , 40, 3, 41, 50, 61, 31, 410, 1337, 1, -30, -324, 414, 13, -15]
    QuickSort(list)
    print(list)