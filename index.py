# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to start the merged list
        dummy = ListNode(0)
        current = dummy
        
        # While both lists are not empty, compare the first elements and add the smaller one to the merged list
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # Add the remaining elements of either list to the merged list
        if l1:
            current.next = l1
        else:
            current.next = l2
        
        # Return the merged list, skipping the dummy node
        return dummy.next
