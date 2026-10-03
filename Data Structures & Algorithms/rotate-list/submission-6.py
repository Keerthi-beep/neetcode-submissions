class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        cnt = 0
        slow = head

        while slow:
            cnt += 1
            slow = slow.next
        print(cnt,k)
        k %= cnt
        if k == cnt or cnt == 1 or k == 0:
            return head

        i = cnt - k
        j = i
        temp = head
        while i>1:
            i -= 1
            temp = temp.next
        print(temp.val)
        new_head = temp.next
        temp.next = None
        slow = new_head
        while slow and slow.next:
            slow = slow.next
        if slow:
            slow.next = head
        return new_head