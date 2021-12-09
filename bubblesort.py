
def BubbleSort(list):
    n = len(list)
    while True:
        swapped = False
        for i in range(1, n):
            if list[i-1] > list[i]:
                tmp = list[i-1]
                list[i-1] = list[i]
                list[i] = tmp
                swapped = True
        if not swapped:
            break
        n -= 1


if __name__ == "__main__" :
    list = [2, 43 , 40, 3, 41, 50, 61, 31, 410, 1337, 1, -30, -324, 414, 13, -15]
    BubbleSort(list)
    print(list)