#Solution 1
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prv
            prv = curr
            curr = nxt
        head = prv
        return head

#Solution 2
