'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''

def getDoublets(myList, referenceNum):
    #sort the list
    n = len(myList)
    leftIndex = 0
    rightIndex = n - 1
    resultList = set(())
    while leftIndex < rightIndex:
        currentSum = myList[leftIndex] + myList[rightIndex] 
        if( currentSum < -referenceNum):
            leftIndex += 1
        elif(currentSum > -referenceNum):
            rightIndex -= 1
        elif(currentSum == -referenceNum):
            resultList.add((myList[leftIndex], myList[rightIndex], referenceNum))
            leftIndex +=1
            rightIndex -=1

    return resultList

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        setsOfTuples = set(())
        listOfLists = []
        for i in range(n-1) :
            if i>0 and nums[i] == nums[i-1]:
                continue
                
            setsOfTuples.update(getDoublets(nums[i+1:], nums[i]))

        listOfLists = [list(tpl) for tpl in setsOfTuples]
        return listOfLists
