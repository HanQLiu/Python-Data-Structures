### Check if 2 sentences are anagrams of each other ###
import unittest

def anagram_check(s1, s2):
    """Check if 2 sentences are anagrams of each other"""
    '''takes 2 sentences and output True or False'''
    s1_letters = []
    s2_letters = []
    for letter in s1:
        if str.isalpha(letter):
            s1_letters.append(str.lower(letter))
    for letter in s2:
        if str.isalpha(letter):
            s2_letters.append(str.lower(letter))

    return sorted(s1_letters) == sorted(s2_letters)

class Test(unittest.TestCase):
    """Test cases"""
    def test_anagram_check(self):
        self.assertTrue(anagram_check("Clint Eastwood", "Old West Action"))
        self.assertTrue(anagram_check("McDonald's restaurants", "Uncle Sam's standard rot"))
        self.assertFalse(anagram_check("Apple", "Microsoft"))


'''run the script'''
if __name__ == '__main__':
    unittest.main()