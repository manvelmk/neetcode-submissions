# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # return value is the head of the output list
        output = ListNode()
        head_ptr = output

        while list1 and list2:
            if list1.val < list2.val:
                head_ptr.next = list1
                list1 = list1.next
            else:
                head_ptr.next = list2
                list2 = list2.next
            
            head_ptr = head_ptr.next

        # now at least one of the lists is empty
        # this makes sure that if one of the lists is
        # non-empty, we append it as-is to the output
        if list1:
            head_ptr.next = list1
        elif list2:
            head_ptr.next = list2

        # since output's head pointer is not used, we need to return the actual head our insertion started at
        return output.next