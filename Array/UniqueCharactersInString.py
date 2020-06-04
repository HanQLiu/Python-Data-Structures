### Given a string,determine if it is comprised of all unique characters ###
import unittest

def unique_characters(just_a_string):
    """Return Ture if all characters in the string is unique else return False"""
    return len(set(just_a_string)) == len(just_a_string)


class Test(unittest.TestCase):
    """Test cases"""

    '''test unique characters'''
    def test_unique_characters(self):
        self.assertEqual(unique_characters("abcdefg"), True)
        self.assertEqual(unique_characters('goo'), False)
        self.assertEqual(unique_characters(''), True)


'''run the script'''
if __name__ == '__main__':
    unittest.main()