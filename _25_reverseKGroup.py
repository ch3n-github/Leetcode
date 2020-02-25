# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:return None
        l=1
        mark=head
        while mark.next:
            l+=1
            mark=mark.next
        if l<k:return head
        n=l//k
        behead=ListNode(-1)
        behead.next=head
        start=behead
        for _ in range(n):
            openl=[]
            for _ in range(k):
                openl.append(start.next)
                start.next=start.next.next
            end=openl[-1].next
            start.next=openl[-1]
            for i in range(1,len(openl)):
                openl[-i].next=openl[-i-1]
            openl[0].next=end
            for _ in range(k):
                start=start.next
        return behead.next