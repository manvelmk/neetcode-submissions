# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_ptr = head
        if not head:
            return
            
        slow_ptr = self._find_pivot(head, slow_ptr)

        tail_list = ListNode()
        prev_ptr = None
        
        if slow_ptr:
            tail_list = slow_ptr.next
            slow_ptr.next = None

        prev_ptr = self._invert_sublist(tail_list, prev_ptr)

        self._reconstruct(head, prev_ptr) 

    def _find_pivot(self, head, slow_ptr):
        # Find the pivot point
        fast_ptr = head.next

        while fast_ptr and fast_ptr.next:
            if slow_ptr:
                slow_ptr = slow_ptr.next
            
            if fast_ptr.next:
                fast_ptr = fast_ptr.next.next
        return slow_ptr

    def _invert_sublist(self, tail_list, prev_ptr):
        # Invert the right half of the list
        while tail_list:
            # keep the next pointer
            temp = tail_list.next
            # reassign the next pointer to the 
            tail_list.next = prev_ptr
            prev_ptr = tail_list
            tail_list = temp
        return prev_ptr

    def _reconstruct(self, head, prev_ptr):
        #Construct the output list
        left = head
        right = prev_ptr

        while right and left:
            temp_left = left.next
            temp_right = right.next
            left.next = right
            right.next = temp_left

            left = temp_left
            right = temp_right
