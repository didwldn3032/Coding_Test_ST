# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head_list = []

        while head != None:
            head_list.append(head.val)
            head = head.next

        return head_list == head_list[::-1]

'''
Runtime: 1267 ms, faster than 46.26% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 46.5 MB, less than 56.49% of Python3 online submissions for Palindrome Linked List.
'''