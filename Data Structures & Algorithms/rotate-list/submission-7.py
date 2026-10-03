class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        len = 1
        temp = head
        while temp.next:
            len += 1
            temp = temp.next

        temp.next = head
        k %= len
        for _ in range(len-k):
            temp = temp.next

        head = temp.next
        temp.next = None
        return head
        