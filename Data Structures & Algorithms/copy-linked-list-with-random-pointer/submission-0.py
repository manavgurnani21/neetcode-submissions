"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        
        node_directory = {}

        current = head

        # pass 1: creating copy of all nodes and making directory
        while current is not None:
            newNode = Node(current.val, current.next, current.random)
            node_directory[current] = newNode
            current = current.next
        
        # pass 2: make connections to copied objects
        current = head
        while current is not None:
            node_directory[current].next = None if current.next is None else node_directory[current.next]
            node_directory[current].random = None if current.random is None else node_directory[current.random]
            current = current.next
        
        return node_directory[head]

        
