# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        pre_node = post_node = head
        while pre_node and pre_node.next:
            pre_node = pre_node.next.next
            post_node = post_node.next
        return post_node


'''
Runtime: 29 ms, faster than 96.54% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.8 MB, less than 55.66% of Python3 online submissions for Middle of the Linked List.
'''