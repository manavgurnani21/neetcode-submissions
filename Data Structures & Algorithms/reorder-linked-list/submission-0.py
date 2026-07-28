# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        # supposed order of operations
        # traverse to tail of list and collect previous node addresses
        # until l and r don't meet:
        # store l's next in temp
        # connect l to r
        # move l to original next
        # connect r to l's currently pointed node
        # r should now point to the previously stored node
        prev_nodes = {}
        current = head
        while current.next is not None:
            prev_nodes[current.next] = current
            current = current.next
        tail = current # end node (right)

        # looping logic
        while head != tail and head.next != tail:
            temp = head.next
            head.next = tail
            head = temp

            tail.next = head
            tail = prev_nodes[tail]
        if head == tail: # even case
            head.next = None # marking end of list
        elif head.next == tail: # odd case
            tail.next = None
        return
