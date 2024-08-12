'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return ""
        if(len(strs) == 1):
            return strs[0]
        
        shortest_string = min(strs, key=len)
        if(shortest_string == ""):
            return ""
        
        index = 0
        common = ""
        while index < len(shortest_string):
            for i in range(len(strs)):
                if(strs[i][index] != shortest_string[index]):
                    return common
            common += shortest_string[index]
            index += 1
            
        return common



