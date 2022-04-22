# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def removeNthFromEnd(self, head , n):
        result = ListNode(0)
        result.next = head

        slow = fast = result

        for i in range(n):
            fast = fast.next
        if not fast:
            return slow.next
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow = slow.next

        return head

print(Solution().removeNthFromEnd([1,2,3,4,5],1))