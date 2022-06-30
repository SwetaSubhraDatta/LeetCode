from typing import Optional
from LL import LL as Linkedlist
from LL import Node as ListNode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_list = Linkedlist()

        val_l1 = 0
        val_l2 = 0
        sum_ = 0
        carry = 0
        while l1 or l2 or carry:
            if l1:
                val_l1 = l1.val
                l1 = l1.next
            if l2:
                val_l2 = l2.val
                l2 = l2.next

            sum_ = val_l1 + val_l2 + carry
            if sum_ // 10 != 0:
                carry = sum_ % 10
            new_list.push(sum_)

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_list = root_list = ListNode(0)
        val_l1 = 0
        val_l2 = 0
        sum_ = 0
        carry = 0
        while l1 or l2 or carry:
            if l1:
                val_l1 = l1.val
                l1 = l1.next
            if l2:
                val_l2 = l2.val
                l2 = l2.next

            sum_ = val_l1 + val_l2 + carry
            if sum_ // 10 != 0:
                carry = sum_ % 10
            new_list.next = ListNode(sum_)
            new_list = new_list.next
        return root_list


Soln = Solution()
ll = Linkedlist()
ll.push(9)
ll.push(5)
ll.push(4)


Soln.addTwoNumbers(ll.start_node, l2=None)
