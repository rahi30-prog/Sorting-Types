import unittest
from Bubble import BubbleSort
from Selection import SelectionSort


class Bubblesort(unittest.TestCase):
    cases = [
        ([5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),
        ([1],[1]),
        ([1, 2, 3, 4, 9], [1, 2, 3, 4, 9])
        ]
    
    def setUp(self):
        self.nochange = [1, 2, 5, 10]
        self.descend = [10, 9, 8, 7]
        self.same = [8, 8, 8]
        self.single = [1]


    def test_steps_BubbleSort(self):
        for test, expectedResult in self.cases:
            self.assertEqual(BubbleSort(test), expectedResult)

    def test_nochange(self):    #defined a function
        nochange_steps = [1, 2, 5, 10]
        self.assertEqual(BubbleSort(self.nochange), nochange_steps)  #used assertequal by linking the Bubblesort algorithm with cases written in the 'setUp' function.

    def test_descend(self):
        descend_steps = [
            [10, 9, 8, 7], [9, 10, 8, 7], [9, 8, 10, 7], [9, 8, 7, 10],
            [8, 9, 7, 10], [8, 7, 9, 10], [7, 8, 9, 10]
            ]
        #start with the given list and then apply the logic of bubble sort later that step!
        self.assertEqual(BubbleSort(self.descend,True), descend_steps)

    def test_same(self):    
        self.assertEqual(BubbleSort(self.same), [8, 8, 8])

    def test_single(self):
        self.assertEqual(BubbleSort(self.single), self.single)

    def test_steps_SelectionSort(self):
        for test, expectedResult in self.cases:
            self.assertEqual(SelectionSort(test), expectedResult)


    def test_NoChange(self):
        NoChange_steps = [1, 2, 5, 10]
        self.assertEqual(SelectionSort(self.nochange), NoChange_steps)

    def test_Descend(self):
        Descend_steps = [[10, 9, 8, 7],
                        [7, 9, 8, 10],
                        [7, 8, 9, 10],
                        [7, 8, 9, 10]
                        ]
        self.assertEqual(SelectionSort(self.descend, True), Descend_steps)


    def test_Same(self):
        Same = [[8, 8, 8]]
        self.assertEqual(SelectionSort(self.same), [8, 8, 8])

    def test_Single(self):
        self.assertEqual(SelectionSort(self.single), self.single)



if __name__ == '__main__':  #as we have imported another module
    unittest.main()     #framework of unit test case, runs the test cases.
