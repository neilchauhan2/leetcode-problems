# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        fast = head
        slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow


    def reverseList(self, head):
        cur = head
        prev = None

        while cur:
            next = cur.next
            cur.next = prev
            
            prev = cur
            cur = next
        
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.getMid(head)
        head2 = self.reverseList(mid)

        while head and head2:
            temp1 = head.next
            temp2 = head2.next

            head.next = head2
            head2.next = temp1

            head = temp1
            head2 = temp2

        return head
        