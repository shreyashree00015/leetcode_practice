# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.traverse(l1,l2)
        return l1
    
    def add_node_at_end(self, head: Optional[ListNode], val: int) -> ListNode:
        new_node = ListNode(val)
        if head is None:
            return new_node

        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return head
    
    def traverse(self, head1: Optional[ListNode], head2: Optional[ListNode]):
        cur = head1
        current1 = head1
        current2 = head2
        carry = 0
        while current1 is not None and current2 is not None:
            tot = current1.val+current2.val+int(carry)
            if len(str(tot))>1:
                carry = int(str(tot)[0])
                cur.val = int(str(tot)[1])
            else:
                cur.val = tot
                carry = 0
            current1 = current1.next
            current2 = current2.next
            if cur.next is None and (current1 is not None or current2 is not None):
                cur.next = ListNode(0)
            cur = cur.next
            
        while current2 is None and current1 is not None:
            tot = current1.val + int(carry)
            if len(str(tot))>1:
                carry = int(str(tot)[0])
                cur.val = int(str(tot)[1])
            else:
                cur.val = tot
                carry = 0
            current1 = current1.next
            if cur.next is None and current1 is not None:
                cur.next = ListNode(0)
            cur = cur.next
        
        while current1 is None and current2 is not None:
            tot = current2.val + int(carry)
            if len(str(tot))>1:
                carry = int(str(tot)[0])
                cur.val = int(str(tot)[1])
            else:
                cur.val = tot
                carry = 0
            current2 = current2.next
            if cur.next is None and current2 is not None:
                cur.next = ListNode(0)
            cur = cur.next
            
        if carry > 0:
            self.add_node_at_end(head1, carry)
        return head1

        