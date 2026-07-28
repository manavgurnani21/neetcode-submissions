# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use a window of n elements, keep going through the end
        if head is None:
            return head
        
        start = head
        start_prev = None
        end = head

        # moving end to start + n - 2
        gap = 0
        while gap < n:
            end = end.next
            gap += 1

        if end is None:
            return head.next

        # traverse to the end of the list (start is at nth element from end of list)
        while end.next is not None:
            start = start.next
            end = end.next

        # remove element at start
        start.next = start.next.next

        return head