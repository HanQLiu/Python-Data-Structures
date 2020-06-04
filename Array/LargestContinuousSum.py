### Given an array of integers and find the largest continuous sum ###
import unittest

def largest_continuous_sum(int_array):
    """Find the largest continuous sum of array"""
    largest_sum = float("-inf")
    for i in range(len(int_array)):
        temp_sum = int_array[i]
        if temp_sum > largest_sum:
            largest_sum = temp_sum
        j = i + 1
        while j < len(int_array):
            temp_sum += int_array[j]
            if temp_sum > largest_sum:
                largest_sum = temp_sum
            j += 1

    return largest_sum


class Test(unittest.TestCase):
    """Test cases"""

    '''test largest continuous sum'''
    def test_largest_continuous_sum(self):
        self.assertEqual(largest_continuous_sum([1,2,-1,3,4,-1]), 9)
        self.assertEqual(largest_continuous_sum([1,2,-1,3,4,10,10,-10,-1]), 29)
        self.assertEqual(largest_continuous_sum([-1,1]), 1)


'''run the script'''
if __name__ == '__main__':
    unittest.main()