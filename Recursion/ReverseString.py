### Given a string and reverse the string ###
import unittest


def reverse_string(string_to_reverse):
    if len(string_to_reverse) == 1:
        return string_to_reverse[0]
    else:
        return string_to_reverse[-1] + reverse_string(string_to_reverse[:-1])


class Test(unittest.TestCase):
    """Test cases"""

    '''test reverse string'''
    def test_reverse_string(self):
        print(reverse_string("test reverse string"))


'''run the script'''
if __name__ == '__main__':
    unittest.main()

