class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dic = {}
        resultList = []

        for s in strs:
            sorted_str = tuple(sorted(s))
            if sorted_str not in anagram_dic.keys():
                anagram_dic[sorted_str] = []

            anagram_dic[sorted_str].append(s)
        
        for val in anagram_dic.values():
            resultList.append(val)
        
        return resultList
