### Check if a singly linked list contains a cycle ###
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def cycle_check(node):
    """Given a starting node, return True if the singly linked list contains a cycle else return False"""
    node_list = []
    current_node = node
    while current_node.next is not None:
        if current_node in node_list:
            return True
        else:
            node_list.append(current_node)
            current_node = current_node.next
    return False


class Test(unittest.TestCase):
    """Test cases"""

    '''test cycle check'''
    def test_cycle_check(self):
        # Group 1
        a = Node(1)
        b = Node(2)
        c = Node(3)
        a.next = b
        b.next = c
        c.next = a

        # Group 2
        x = Node(1)
        y = Node(2)
        z = Node(3)
        x.next = y
        y.next = z

        self.assertTrue(cycle_check(a))
        self.assertFalse(cycle_check(x))


'''run the script'''
if __name__ == '__main__':
    unittest.main()

