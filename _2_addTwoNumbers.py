# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Author：chen
class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def list_to_node(l):#列表转换为链表
            node=ListNode(l[0])
            pre=node
            for i in l[1:]:
                pre.next=ListNode(i)
                pre=pre.next
            return node
        def node_to_int(node):#链表转换为数字
            i=0
            t=0
            while node:
                i+=node.val*10**t
                t+=1
                node=node.next
            return i
        return list_to_node(list(str((node_to_int(l1)+node_to_int(l2))))[::-1])