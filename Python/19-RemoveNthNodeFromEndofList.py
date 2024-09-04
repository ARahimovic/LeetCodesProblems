'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# remove last node
def removeLastNode(head):
    #no element or one element on the list
    if head is None or head.next is None:
        return None
    temp = head
    #get the before last node
    while(temp.next.next is not None):
        temp = temp.next
    
    temp.next = None
    return head
    

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None :
            return None

        # remove the last node
        if n == 1:  
            return removeLastNode(head)

        rightPtr = head
        leftPtr = head

        #get diff between leftPtr and rightPtr
        for _ in range(n):
            rightPtr = rightPtr.next
        
        # we are deleting the first node
        if rightPtr is None :
            return head.next

        #get the last node
        while(rightPtr.next is not None):
            leftPtr = leftPtr.next
            rightPtr = rightPtr.next


        leftPtr.next = leftPtr.next.next 
        
        return head