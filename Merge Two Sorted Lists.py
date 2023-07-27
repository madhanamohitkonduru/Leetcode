#Actual code
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next



#my try which is wrong
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None or (list1 == None and list2 == None):
            return list2
        elif list2 == None:
            return list1
        else:
            if list1.val <= list2.val:
                current1, current2 = list1, list2
            else:
                current1, current2 = list2, list1
            head, current = None, current1

        while current1 or current2:
            print(head)
            if current1.next == None:
                current.next = current2
                break
            elif current2.next == None:
                current.next = current1
                break

            if current1.next.val <= current2.val:
                current.next = current1.next
                current = current.next
                current1 = current1.next
            else:
                current.next = current2
                current = current.next
                current2 = current2.next
        return head