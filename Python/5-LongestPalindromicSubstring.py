'''
Given a string s, return the longest palindromic substringin s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"


Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s :
            return ""
        if(len(s) == 1):
            return s

        resultString = ""
        for index, char in enumerate(s):
            secondOccurance = s.find(char, index+1)
            while(secondOccurance != -1):
                substring = s[index:secondOccurance+1]
                reversedSubstring = substring[::-1] 
                if substring == reversedSubstring:
                    if(len(substring) > len(resultString)):
                        resultString = substring
                
                secondOccurance = s.find(char, secondOccurance+1)
        
        if not resultString :
            return s[0]
            
        return resultString
    