# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_list=[]
        while head: #node.next =None이 아닐 경우. 즉, node의 next가 있는 경우 실행
            node_list.append(head.val)
            head=head.next
        if node_list==node_list[-1]:
            return True
        else:
            return False

# Runtime: 1022 ms, faster than 71.48% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 46.5 MB, less than 56.58% of Python3 online submissions for Palindrome Linked List.