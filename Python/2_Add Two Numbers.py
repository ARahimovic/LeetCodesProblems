'''
ou are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1] 
'''


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def __init__(self):
        self.carry = 0

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2 and self.carry == 0 :
            return None
        
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        result = l1_val + l2_val + self.carry

        self.carry = result // 10
        result = result % 10

        new_node = ListNode(result)
        new_node.next = self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None)
        
        return new_node 