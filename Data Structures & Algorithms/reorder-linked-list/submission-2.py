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
            
        fast_ptr = head.next

        while fast_ptr and fast_ptr.next:
            if slow_ptr:
                slow_ptr = slow_ptr.next
            
            if fast_ptr.next:
                fast_ptr = fast_ptr.next.next

        tail_list = ListNode()
        prev_ptr = None
        
        if slow_ptr:
            tail_list = slow_ptr.next
            slow_ptr.next = None

        # Invert the right half of the list
        while tail_list:
            # keep the next pointer
            temp = tail_list.next
            # reassign the next pointer to the 
            tail_list.next = prev_ptr
            prev_ptr = tail_list
            tail_list = temp

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
