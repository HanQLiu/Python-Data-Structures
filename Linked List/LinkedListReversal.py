### Reverse a singly linked list ###
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_SLList(node):
    """The function will take in the head of a singly linked list and return the new head of reversed list"""
    list_of_nodes = []
    current_node = node
    # append all nodes
    while current_node.next is not None:
        list_of_nodes.append(current_node)
        current_node = current_node.next
    list_of_nodes.append(current_node)

    list_of_nodes.reverse()

    for i in range(len(list_of_nodes) - 1):
        list_of_nodes[i].next = list_of_nodes[i + 1]
    list_of_nodes[i + 1].next = None
    return list_of_nodes[0]


class Test(unittest.TestCase):
    """Test cases"""

    '''test reverse singly linked list'''
    def test_reverse_SLList(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        a.next = b
        b.next = c
        c.next = d
        reverse_SLList(a)

        print(d.next.value)
        print(c.next.value)
        print(b.next.value)

        self.assertIsNone(a.next)

'''run the script'''
if __name__ == '__main__':
    unittest.main()

