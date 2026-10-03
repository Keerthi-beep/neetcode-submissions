# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        cnt = 0
        while slow:
            cnt += 1
            slow = slow.next
        
        slow = head
        diff = cnt-n
        if diff == 0:
            return head.next
        while diff>1:
            slow = slow.next
            diff -= 1
        if slow.next:
            slow.next = slow.next.next
        return head