# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n==0 or not head:return head
        listnode=head
        l=1
        while listnode.next!=None:
            x=listnode.next
            listnode=x
            l+=1
        if l==1:return None
        if l==n:return head.next
        listnode=head
        for i in range(l-n-1):
            x=listnode.next
            listnode=x
        listnode.next=listnode.next.next
        return head