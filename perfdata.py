import timeit

def timeSort(array, sortFunc):
    start = timeit.default_timer()
    if sortFunc == None:
        array.sort()
    else:
        sortFunc(array)
    end = timeit.default_timer()
    return end-start

class PerformaceData():
    def __init__(self, func, title):
        self.function = func
        self.title = title
        self.unsorted = []
        self.sorted = []
        self.reversed = []
        self.almost = []
        self.element_counts = []

    def enrichUnsorted(self, array):
        self.unsorted.append(timeSort(array, self.function))

    def enrichSorted(self, array):
        self.sorted.append(timeSort(array, self.function))

    def enrichReversed(self, array):
        self.reversed.append(timeSort(array, self.function))

    def enrichAlmostSorted(self, array):
        self.almost.append(timeSort(array, self.function))

    def enrichElementCount(self, count):
        self.element_counts.append(count)