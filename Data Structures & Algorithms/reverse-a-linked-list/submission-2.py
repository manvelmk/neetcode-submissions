# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None #head can not have a previous node
        curNode = head

        while curNode:
            # maintain reference to the next pointer before overwriting it
            tempNext = curNode.next

            curNode.next = prevNode
            prevNode = curNode
            curNode = tempNext
        
        return prevNode