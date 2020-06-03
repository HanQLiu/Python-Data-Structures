import unittest

class QueueWith2Stacks:
    """Implementation"""
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) != 0:
                self.out_stack.append(self.in_stack.pop())

        if len(self.out_stack) > 0:
            return self.out_stack.pop()
        else:
            print("Popping from empty stack")

    def output(self):
        while len(self.in_stack) != 0:
            self.out_stack.append(self.in_stack.pop())
        return_string = []
        for item in self.out_stack:
            return_string.append(str(item))

        if len(return_string) > 0:
            return ' '.join(return_string)
        else:
            return "It's an empty stack"

class Test(unittest.TestCase):
    """Test cases"""

    '''test enqueue'''
    def test_enqueue(self):
        q2s = QueueWith2Stacks()
        q2s.enqueue(1)
        q2s.enqueue(2)
        q2s.enqueue(3)

        self.assertEqual(q2s.output(), "3 2 1")

    '''test dequeue'''
    def test_dequeue(self):
        q2s = QueueWith2Stacks()
        q2s.enqueue(1)
        q2s.enqueue(2)
        q2s.enqueue(3)
        q2s.dequeue()

        self.assertEqual(q2s.output(), "3 2")


'''run the script'''
if __name__ == '__main__':
    unittest.main()

