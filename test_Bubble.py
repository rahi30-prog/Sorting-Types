import unittest
from Bubble import BubbleSort
from Selection import SelectionSort

# Test cases
cases = [
    ([5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),
    ([1], [1]),
    ([1, 2, 3, 4, 9], [1, 2, 3, 4, 9])
]

# Test data
nochange = [1, 2, 5, 10]
descend = [10, 9, 8, 7]
same = [8, 8, 8]
single = [1]

class TestSortingAlgorithms(unittest.TestCase):
    
    def test_steps_BubbleSort(self):
        for test, expectedResult in cases:
            self.assertEqual(BubbleSort(test), expectedResult)

    def test_nochange(self):
        nochange_steps = [1, 2, 5, 10]
        self.assertEqual(BubbleSort(nochange), nochange_steps)

    def test_descend(self):
        descend_steps = [
            [10, 9, 8, 7], [9, 10, 8, 7], [9, 8, 10, 7], [9, 8, 7, 10],
            [8, 9, 7, 10], [8, 7, 9, 10], [7, 8, 9, 10]
        ]
        self.assertEqual(BubbleSort(descend, True), descend_steps)

    def test_same(self):
        self.assertEqual(BubbleSort(same), [8, 8, 8])

    def test_single(self):
        self.assertEqual(BubbleSort(single), single)

    def test_steps_SelectionSort(self):
        for test, expectedResult in cases:
            self.assertEqual(SelectionSort(test), expectedResult)

    def test_NoChange(self):
        NoChange_steps = [1, 2, 5, 10]
        self.assertEqual(SelectionSort(nochange), NoChange_steps)

    def test_Descend(self):
        Descend_steps = [
            [10, 9, 8, 7], [7, 9, 8, 10],
            [7, 8, 9, 10], [7, 8, 9, 10]
        ]
        self.assertEqual(SelectionSort(descend, True), Descend_steps)

    def test_Same(self):
        self.assertEqual(SelectionSort(same), [8, 8, 8])

    def test_Single(self):
        self.assertEqual(SelectionSort(single), single)

if __name__ == '__main__':
    unittest.main()
