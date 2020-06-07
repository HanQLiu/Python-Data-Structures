### Given a string, output a list of all the possible permutations of that string ###
import unittest


def permute(s):
    """input 'abc', should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']"""
    out = []
    if len(s) == 1:
        out = [s]
    else:
        for i, letter in enumerate(s):
            for perm in permute(s[:i] + s[i + 1:]):
                out += [letter + perm]
    return out


class Test(unittest.TestCase):
    """Test cases"""

    '''test permute'''
    def test_permute(self):
        self.assertEqual(permute('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(permute('dog'), ['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god'])


'''run the script'''
if __name__ == '__main__':
    unittest.main()

