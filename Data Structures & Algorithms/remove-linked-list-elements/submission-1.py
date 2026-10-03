# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        prev = head
        while temp:
            if temp.val == val:
                if temp == head:
                    head = temp.next
                else:
                    prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return head