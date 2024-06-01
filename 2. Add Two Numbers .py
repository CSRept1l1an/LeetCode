from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    curr = head
    carry = 0

    while l1 or l2:
        sum_val = carry

        if l1:
            sum_val = sum_val + l1.val
            l1 = l1.next

        if l2:
            sum_val = sum_val + l2.val
            l2 = l2.next

        carry = sum_val // 10



class Solution:
    pass
