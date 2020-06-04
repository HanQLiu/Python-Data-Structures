### Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4' ###
import unittest

def compress_string(just_a_string):
    """Shrink 'AAAABBBBCCCCCDDEEEE' to 'A4B4C5D2E4'"""
    string_dict = dict()
    for letter in just_a_string:
        if letter in string_dict:
            string_dict[letter] += 1
        else:
            string_dict[letter] = 1

    string_builder = ""
    for key, value in string_dict.items():
        string_builder += f"{key}{value}"

    return string_builder


class Test(unittest.TestCase):
    """Test cases"""

    '''test compress string'''
    def test_compress_string(self):
        self.assertEqual(compress_string('AAAABBBBCCCCCDDEEEE'), "A4B4C5D2E4")
        self.assertEqual(compress_string('AAABCCDDDDD'), 'A3B1C2D5')
        self.assertEqual(compress_string(''), '')


'''run the script'''
if __name__ == '__main__':
    unittest.main()