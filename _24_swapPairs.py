# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:return None
        if head.next==None:return head
        behead=ListNode(-1)
        behead.next=head
        c=behead
        while c.next and c.next.next:
            a,b=c.next,c.next.next
            c.next,a.next=b,b.next
            b.next=a
            c=c.next.next
        return behead.next