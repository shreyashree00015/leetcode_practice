# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        head3 = list3 = ListNode()
        while head1 and head2:
            if head1.val<head2.val:
                head3.next = head1
                head1, head3 = head1.next, head1
            elif head1.val>head2.val:
                head3.next = head2
                head2, head3 = head2.next, head2
            else:
                head3.next = head1
                head1, head3 = head1.next, head1
                head3.next = head2
                head2, head3 = head2.next, head2
        while head1:
            head3.next = head1
            head1, head3 = head1.next, head1
        while head2:
            head3.next = head2
            head2, head3 = head2.next, head2
        return list3.next