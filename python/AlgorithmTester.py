import numpy as np
from math import ceil
from QuickSortHoarePartitionScheme import QuickSort as QuickSortHoare
import matplotlib.pyplot as plt


class AlgorithmTester:
    def __init__(self, size, iteration):
        self.size = size
        self.iterations = iteration

    def generate(self):
        arr = list(np.random.randint(0, ceil(self.size / 2), self.size))
        return arr

    def verify_qs_hoare(self):
        qs_calls_values = np.arange(self.iterations)
        ok = True

        for i in range(self.iterations):
            arr = self.generate()
            qs = QuickSortHoare(arr)
            result = qs.sortAndVerify()
            qs_calls_values[i] = qs.counter

            if not result:
                qs.print_report()
                ok = False
        if ok:
            print("Sorting succesfull!")
            self.generate_calls_plot(qs_calls_values)
        else:
            print("There were errors")

    def generate_calls_plot(self, array):
        plt.hist(array)
        plt.ylabel("Number of occurrences")
        plt.title('QuickSort method calls')
        plt.show()

tester = AlgorithmTester(30, 50)
tester.verify_qs_hoare()