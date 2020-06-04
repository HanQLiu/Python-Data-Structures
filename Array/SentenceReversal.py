### Given a string of words, reverse all the words ###
import unittest


def reverse_sentence(sentence):
    """Takes a string of words, reverse all the words"""
    return ' '.join(sentence.split()[::-1])


class Test(unittest.TestCase):
    """Test cases"""

    '''test reverse sentence'''
    def test_reverse_sentence(self):
        self.assertEqual(reverse_sentence("Hi John,   are you ready to go?"), "go? to ready you are John, Hi")
        self.assertEqual(reverse_sentence("   Hello John    how are you   "), "you are how John Hello")
        self.assertEqual(reverse_sentence('1'), '1')


'''run the script'''
if __name__ == '__main__':
    unittest.main()

