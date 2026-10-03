# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0:
            return head
        slow = head
        length = 1
        while slow and slow.next:
            length += 1
            slow = slow.next
        if k == length:
            return head
        slow.next = head
        print(length)

        k %= length
        c = length-k
        while c>0:
            slow = slow.next
            c -= 1
        head = slow.next
        slow.next = None
        return head