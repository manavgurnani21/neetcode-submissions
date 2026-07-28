# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # new memory-optimized solution
        # constant memory means storing a static number of nodes
        # runner theory (leader and follower)
            # if the leader goes 2 step and follower goes 1 steps:
            # there's a cycle if leader and follower meet
        if head is None:
            return False
        leader = head
        follower = head
        while leader.next is not None and leader.next.next is not None and follower.next is not None:
            leader = leader.next.next
            follower = follower.next
            if leader == follower:
                return True
        return False