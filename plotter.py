
import matplotlib.pyplot as plt

def PlotPerformanceData(perf):
    plt.plot(perf.element_counts, perf.unsorted, label="unsorted", marker="o")
    plt.plot(perf.element_counts, perf.sorted, label="sorted", marker="o")
    plt.plot(perf.element_counts, perf.reversed, label="reversed", marker="o")
    plt.plot(perf.element_counts, perf.almost, label="almost", marker="o")
    plt.xscale('log', base=2)
    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.title(perf.title)
    plt.legend()
    plt.savefig("graphs/"+perf.title+".png")
    plt.close()

def PlotUnsorted(perfs):
    for d in perfs: plt.plot(d.element_counts, d.unsorted, label=d.title, marker="o")
    plt.xscale('log', base=2)
    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.title("Sort time for unsorted array")
    plt.legend()
    plt.savefig("graphs/unsorted.png")
    plt.close()

def PlotSorted(perfs):
    for d in perfs: plt.plot(d.element_counts, d.sorted, label=d.title, marker="o")
    plt.xscale('log', base=2)
    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.title("Sort time for sorted array")
    plt.legend()
    plt.savefig("graphs/sorted.png")
    plt.close()

def PlotReversed(perfs):
    for d in perfs: plt.plot(d.element_counts, d.reversed, label=d.title, marker="o")
    plt.xscale('log', base=2)
    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.title("Sort time for reverse-sorted array")
    plt.legend()
    plt.savefig("graphs/reversed.png")
    plt.close()

def PlotAlmostSorted(perfs):
    for d in perfs: plt.plot(d.element_counts, d.almost, label=d.title, marker="o")
    plt.xscale('log', base=2)
    plt.xlabel("Array Size")
    plt.ylabel("Time (s)")
    plt.title("Sort time for almost sorted array")
    plt.legend()
    plt.savefig("graphs/almost_sorted.png")
    plt.close()

def PlotPerfs(perfs):
    for d in perfs : PlotPerformanceData(d)
    PlotUnsorted(perfs)
    PlotSorted(perfs)
    PlotReversed(perfs)
    PlotAlmostSorted(perfs)