# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        offsetNode = ListNode(0, head)
        offset = n

        left_ptr = offsetNode
        right_ptr = head # start the right pointer at the head

        # then loop to find the last ListNode
        while offset > 0 and right_ptr:
            right_ptr = right_ptr.next
            offset -= 1
        
        # Move both pointers until right pointer reaches the end of the list
        while right_ptr and left_ptr:
            left_ptr = left_ptr.next
            right_ptr = right_ptr.next

        if left_ptr and left_ptr.next:
            left_ptr.next = left_ptr.next.next

        return offsetNode.next