# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Runtime: 44 ms, faster than 62.70% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.9 MB, less than 55.99% of Python3 online submissions for Middle of the Linked List.
