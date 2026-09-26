# Given the head of a singly linked list, determine whether it reads the
# same forwards and backwards.
# Example: [1,2,2,1] -> Output: True

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def build_linked_list(values):
    head = Node(values[0])
    current = head
    