### takes a head node and an integer value n and then returns the nth to last node in the singly linked list ###
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def nth_to_last_node(head, n):
    """Takes a head node and an int n, returns the nth to last node in the singly linked list"""
    nodes_list = []
    current_node = head
    while current_node.next is not None:
        nodes_list.append(current_node)
        current_node = current_node.next
    nodes_list.append(current_node)

    return nodes_list[len(nodes_list) - n]


class Test(unittest.TestCase):
    """Test cases"""

    '''test nth to last node'''
    def test_nth_to_last_node(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        e = Node(5)

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        self.assertEqual(nth_to_last_node(a, 2), d)
        self.assertEqual(nth_to_last_node(a, 4), b)
        self.assertEqual(nth_to_last_node(a, 3), c)

'''run the script'''
if __name__ == '__main__':
    unittest.main()

