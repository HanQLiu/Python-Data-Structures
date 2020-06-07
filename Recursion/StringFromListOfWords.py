### Split a string to see if it is able to make up words from a list ###
import unittest
from itertools import permutations

def word_split(string_of_chars, a_list_of_words):
    """Takes a string of chars and a list of words as inputs"""
    lens_of_a_list_of_words = list(range(len(a_list_of_words)))  # [1, 2, 3, 4, 5, 6]
    return_list = None
    for length in lens_of_a_list_of_words:
        perms = list(permutations(a_list_of_words, length + 1))
        perms_strings = perms.copy()
        for i in range(len(perms)):
            perms_strings[i] = ''.join(perms_strings[i])
        for i in range(len(perms_strings)):
            if string_of_chars == perms_strings[i]:
                return_list = perms[i]
    return list(return_list) if return_list is not None else []



class Test(unittest.TestCase):
    """Test cases"""

    '''test word split'''
    def test_word_split(self):
        self.assertEqual(word_split('themanran', ['the', 'ran', 'man']), ['the', 'man', 'ran'])
        self.assertEqual(word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']),
                         ['i', 'love', 'dogs', 'John'])
        self.assertEqual(word_split('themanran',['clown','ran','man']), [])


'''run the script'''
if __name__ == '__main__':
    unittest.main()

