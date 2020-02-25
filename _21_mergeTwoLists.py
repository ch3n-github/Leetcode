# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:return None
        nums=[]
        while l1!=None:
            nums.append(l1.val)
            l1=l1.next
        while l2!=None:
            nums.append(l2.val)
            l2=l2.next
        nums.sort()
        head=ListNode(nums[0])
        headnext=head
        for i in range(1,len(nums)):
            headnext.next=ListNode(nums[i])
            headnext=headnext.next
        return head