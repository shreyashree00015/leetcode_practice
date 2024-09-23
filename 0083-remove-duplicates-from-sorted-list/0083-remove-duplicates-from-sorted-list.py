# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h1 = head
        while head is not None and head.next is not None:
            cur = head.val
            next_ele = head.next.val
            # snext_ele = head.next.next.val
            if cur!=next_ele:
                head = head.next
            else:
                head.next = head.next.next
        return h1