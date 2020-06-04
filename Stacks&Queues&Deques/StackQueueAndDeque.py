### Implementations of Stack, Queue, and Deque ###
import unittest

"""Implementation of Stack"""
class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)

"""Implementation of Queue"""
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, element):
        self.queue.insert(0, element)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

"""Implementation of Deque"""
class Deque:
    def __init__(self):
        self.deque = []

    def is_empty(self):
        return self.deque == []

    def add_front(self, element):
        self.deque.insert(0, element)

    def add_rear(self, element):
        self.deque.append(element)

    def remove_front(self):
        return self.deque.pop(0)

    def remove_rear(self):
        return self.deque.pop()

    def size(self):
        return len(self.deque)


"""Implementation of queue using 2 stacks"""
class QueueWith2Stacks:
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
    """Test cases of QueueWith2Stacks"""

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

