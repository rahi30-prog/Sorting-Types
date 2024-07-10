import unittest
from Selection import SelectionSort

class TestSelectionSortingAlgorithms(unittest.TestCase):
#TEST CASES:
    def test_SelectionSort(self):
            cases = [                               #Test cases
            ([5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),
            ([1], [1]),
            ([1, 2, 3, 4, 9], [1, 2, 3, 4, 9])
            ]

            for test, expectedResult in cases:
                self.assertEqual(SelectionSort(test), expectedResult)

    def test_descend(self):
        descend = [10, 9, 8, 7]  #Test Data
        descend_steps = [
            [10, 9, 8, 7], [7, 9, 8, 10], [7, 8, 9, 10], [7, 8, 9, 10]
                        ]              #Expected steps
        self.assertEqual(SelectionSort(descend, True), descend_steps)


    def test_NoChange(self):
        nochange = [1, 2, 5, 10]    #Test Data
        self.assertEqual(SelectionSort(nochange), [1, 2, 5, 10])


    def test_Same(self):    
        same = [8, 8, 8]    #Test Data    
        self.assertEqual(SelectionSort(same), same)


    def test_Single(self):
        single = [1]     #Test Data
        self.assertEqual(SelectionSort(single), single)

if __name__ == '__main__':
    unittest.main()
