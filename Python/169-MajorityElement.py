'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        myDict = {}
        for x in nums:
            myDict[x] = myDict.get(x, 0) + 1
            if  myDict[x] > n/2 :
                return x 
        