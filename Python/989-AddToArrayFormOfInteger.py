'''
The array-form of an integer num is an array representing its digits in left to right order.
For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

Example 1:
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
'''

## take to much time and not python specific

# class Solution:
#     def addToArrayForm(self, num: List[int], k: int) -> List[int]:
#         intNum = 0
#         n = len(num)
#         for i in range(n-1,-1,-1):
#             intNum+= num[i] * pow(10,n-1-i)
        
#         result = intNum + k
#         resultList = []
#         while result != 0 :
#             resultList.append(result % 10)
#             result //= 10

#         resultList.reverse()
#         return resultList


import sys
# Increase the maximum number of digits allowed for integer string conversion
sys.set_int_max_str_digits(10000) 

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        #convert the int array to string then convert the string to an int
        myInt = int(''.join(map(str, num)))
        result = myInt + k
        #reconvert the result to string then make a list of each char
        resultList = [int(digit) for digit in str(result)]
        return resultList
        

        