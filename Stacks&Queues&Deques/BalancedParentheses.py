### Given a string of opening and closing parentheses, check whether it’s balanced ###
import unittest

def check_parentheses_balance(just_a_string_w_parens):
    open_parens = '{[('
    close_parens = '}])'
    parens_stack = []
    for char in just_a_string_w_parens:
        if char in open_parens:
            parens_stack.append(open_parens.index(char))
        if char in close_parens:
            if close_parens.index(char) != parens_stack.pop():
                return False
    return True if len(parens_stack) == 0 else False


class Test(unittest.TestCase):
    """Test cases"""

    '''test check parentheses balance'''
    def test_check_parentheses_balance(self):
        self.assertTrue(check_parentheses_balance('[{{{(())}}}]((()))'))
        self.assertFalse(check_parentheses_balance('[](){([[[]]])}('))
        self.assertFalse(check_parentheses_balance('[[[]])]'))


'''run the script'''
if __name__ == '__main__':
    unittest.main()

