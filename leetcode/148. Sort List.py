# Recursion - merge sort top down

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        fast = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(fast)
        return self.merge(left, right)

    def merge(self, l, r):
        dummy = curr = ListNode()
        while l and r:
            if l.val < r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next

        if l:
            curr.next = l
        else:
            curr.next = r

        return dummy.next

# None-Recursion bottom up
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1

        dummy = ListNode(0)
        dummy.next = head
        step = 1
        while step < count:
            curr = dummy.next
            tail = dummy
            while curr:
                l = curr
                r = self.split(l, step)
                curr = self.split(r, step)
                tail = self.merge(l, r, tail)

            step <<= 1

        return dummy.next


    # break lst into two at step, and return the head of the second list
    def split(self, lst, step):
        curr = lst
        i = 1
        while curr and i < step:
            curr = curr.next
            i += 1

        if curr:
            ret = curr.next
            curr.next = None
            return ret
        else:
            return None

    # merge sort l and r and link to head, and move head to the last element
    def merge(self, l, r, head):
        curr = head
        while l and r:
            if l.val < r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next
            curr = curr.next

        if l:
            curr.next = l
        else:
            curr.next = r

        while curr.next:
            curr = curr.next

        return curr
