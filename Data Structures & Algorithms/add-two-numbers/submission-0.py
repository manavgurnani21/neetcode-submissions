# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # - start by traversing through both numbers
        # - add with carry (reset carry after adding)
        # - stop when one of the numbers ends have reached
        #     - finish adding rest of digits if needed
        # - handle final sum (> 9 case)
        carry = 0
        curr_sum = 0
        result_head = ListNode(val=-1)
        current_res = result_head
        l1_val = l1.val
        l2_val = l2.val
        while l1 is not None or l2 is not None:
            curr_sum = l1_val + l2_val + carry
            current_res.next = ListNode(val=(curr_sum % 10))
            current_res = current_res.next
            carry = curr_sum // 10
            l1_val = 0 if l1 is None or l1.next is None else l1.next.val
            l2_val = 0 if l2 is None or l2.next is None else l2.next.val
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if curr_sum >= 10:
            current_res.next = ListNode(val=(curr_sum // 10))
            current_res = current_res.next

        print(curr_sum)
        print(carry)
        return result_head.next