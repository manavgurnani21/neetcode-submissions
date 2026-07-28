# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newHead = ListNode()
        current = newHead
        # main idea: process one node at a time and pick the smallest one at each iteration
        while list1 is not None or list2 is not None:
            replacement = None
            if list1 is None:
                replacement = list2
                list2 = list2.next
            elif list2 is None:
                replacement = list1
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    replacement = list1
                    list1 = list1.next
                else:
                    replacement = list2
                    list2 = list2.next
            
            current.next = replacement
            current = current.next
        
        return newHead.next