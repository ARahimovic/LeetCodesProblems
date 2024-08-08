def find_common_prefix_length(str1, str2):
    if not str1 or not str2 :
        return 0
    
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        if(str1[i] != str2[i]):
            return i
    
    return min_len

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        if not arr1 or not arr2 :
            return 0
        
        str_arr1 = list(map(str, arr1))
        str_arr2 = list(map(str, arr2))
        
        max_len = 0

        for str1 in str_arr1:
            for str2 in str_arr2:
                currentLen = find_common_prefix_length(str1, str2)
                if(currentLen > max_len):
                    max_len = currentLen
        
        return max_len






    