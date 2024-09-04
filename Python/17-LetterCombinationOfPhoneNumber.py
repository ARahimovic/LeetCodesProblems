from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digiDict = {
            "2":"abc", 
            "3":"def", 
            "4":"ghi", 
            "5":"jkl", 
            "6":"mno", 
            "7":"pqrs", 
            "8":"tuv", 
            "9":"wxyz"
        }
        
        listOfLists = []
        resultList = []

        for key in digits:
            listOfLists.append(list(digiDict[key]))
        
        
        resultList = [''.join(combination) for combination in product(*listOfLists)]
        return resultList
