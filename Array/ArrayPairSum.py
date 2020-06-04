### Given an integer array, output all the unique pairs that sum up to a specific value k ###
import unittest

def pair_sum(num_list, sum):
    """Takes a list of integers and output unique pairs that sum up to a sum"""
    combos = []
    for i in range(len(num_list)):
        j = i + 1
        while j < len(num_list):
            if num_list[i] + num_list[j] == sum:
                if num_list[i] <= num_list[j] and (num_list[i], num_list[j]) not in combos:
                    combos.append((num_list[i], num_list[j]))
                elif num_list[i] > num_list[j] and (num_list[j], num_list[i]) not in combos:
                    combos.append((num_list[j], num_list[i]))
            j += 1

    return combos


class Test(unittest.TestCase):
    """Test cases"""

    '''test pair sum'''
    def test_pair_sum(self):
        self.assertEqual(pair_sum([1,2,3,1],3), [(1, 2)])
        self.assertEqual(pair_sum([1,3,2,2],4), [(1, 3), (2, 2)])
        self.assertEqual(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10), [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (-1, 11)])


'''run the script'''
if __name__ == '__main__':
    unittest.main()