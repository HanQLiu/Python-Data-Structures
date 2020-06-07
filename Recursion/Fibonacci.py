### Recursion Fibonacci ###
import unittest


def fibonacci_recursion(n):
    """Non-Memoization Version"""
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


fib_memo = dict()


def fib_rec_memoization(n):
    """Memoization Version"""
    if n == 1:
        return 1
    elif n == 0:
        return 0
    if n not in fib_memo:
        fib_memo[n] = fib_rec_memoization(n - 1) + fib_rec_memoization(n - 2)
    return fib_memo[n]


class Test(unittest.TestCase):
    """Test cases"""

    '''test fibonacci recursion'''
    def test_fibonacci_recursion(self):
        self.assertEqual(fibonacci_recursion(10), 55)
        self.assertEqual(fib_rec_memoization(10), 55)
        self.assertEqual(fibonacci_recursion(1), 1)
        self.assertEqual(fib_rec_memoization(1), 1)
        self.assertEqual(fibonacci_recursion(23), 28657)
        self.assertEqual(fib_rec_memoization(23), 28657)


'''run the script'''
if __name__ == '__main__':
    unittest.main()

