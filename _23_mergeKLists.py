# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return None
        nums=[]
        for l in lists:
            while l!=None:
                nums.append(l.val)
                l=l.next
        nums.sort()
        if not nums:return None
        head=ListNode(nums[0])
        nexthead=head
        for i in range(1,len(nums)):
            nexthead.next=ListNode(nums[i])
            nexthead=nexthead.next
        return head