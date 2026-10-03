class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return
        slow=fast=head
        for _ in range(n):
            fast=fast.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next
        # if fast:
        #     print('hi')
        if slow==head and fast==None:
            head=head.next
        elif slow.next:
            slow.next=slow.next.next
            
        return head