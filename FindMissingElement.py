### Find 2 arrays, find which element is missing in the second array ###
import unittest

def find_missing_element(array1, array2):
    """return the one element missing from array2"""
    for element in array2:
        array1.remove(element)
    return array1[0]


class Test(unittest.TestCase):
    """Test cases"""

    '''test find missing element'''
    def test_find_missing_element(self):
        self.assertEqual(find_missing_element([5,5,7,7],[5,7,7]), 5)
        self.assertEqual(find_missing_element([1,2,3,4,5,6,7],[3,7,2,1,4,6]), 5)
        self.assertEqual(find_missing_element([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]), 6)


'''run the script'''
if __name__ == '__main__':
    unittest.main()