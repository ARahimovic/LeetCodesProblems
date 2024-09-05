'''
You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        nodeList = []
        temp = head
        while temp is not None :
            nodeList.append(temp.val)
            temp = temp.next
        
        n = len(nodeList)
        tempVal = nodeList[k-1]
        nodeList[k-1] = nodeList[n-k]
        nodeList[n-k] = tempVal


        temp = head
        for i in range(n):
            if i == k-1 or i == n-k:
                temp.val = nodeList[i]
                
            temp = temp.next

        return head