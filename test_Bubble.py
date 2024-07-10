import unittest
from Bubble import BubbleSort
from Selection import SelectionSort

class TestSortingAlgorithms(unittest.TestCase):
    
    def test_steps_BubbleSort(self):
        cases = [                               #Test cases
        ([5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),
        ([1], [1]),
        ([1, 2, 3, 4, 9], [1, 2, 3, 4, 9])
        ]
        #Bubble Sort
        for test, expectedResult in cases:
            self.assertEqual(BubbleSort(test), expectedResult)
        #Selection Sort
        for test, expectedResult in cases:
            self.assertEqual(SelectionSort(test), expectedResult)


    def test_nochange(self):
        nochange = [1, 2, 5, 10]    #Test Data
        nochange_steps = [1, 2, 5, 10]  #Expected output for the test
        self.assertEqual(BubbleSort(nochange), nochange_steps)
        self.assertEqual(SelectionSort(nochange), [1, 2, 5, 10])


    def test_Same(self):
        same = [8, 8, 8]    #Test Data
        self.assertEqual(BubbleSort(same), same)    #The output is similar to the test data
        self.assertEqual(SelectionSort(same), [8, 8, 8])


    def test_Single(self):
        single = [1]     #Test Data
        self.assertEqual(BubbleSort(single), single)    #The output is similar to the test data
        self.assertEqual(SelectionSort(single), [1])


    def test_descend(self):
        descend = [10, 9, 8, 7]  #Test Data
        descend_steps = [
            [10, 9, 8, 7], [9, 10, 8, 7], [9, 8, 10, 7], [9, 8, 7, 10],
            [8, 9, 7, 10], [8, 7, 9, 10], [7, 8, 9, 10]
        ]              #Expected steps
        self.assertEqual(BubbleSort(descend, True), descend_steps)

if __name__ == '__main__':
    unittest.main()
