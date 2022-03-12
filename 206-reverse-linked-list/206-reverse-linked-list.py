# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode()
        if head is None:
            return None
        
        if head.next is None:
            return head
        
        newNode = head.next
        head.next = None
        node2 = self.reverseList(newNode)
        newNode.next = head
        return node2
        
        
        
        
        
        