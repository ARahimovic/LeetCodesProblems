'''
Given a string representing a sentence with words separated by 
spaces, determine if it is "balanced": the number of words before 
the middle of the sentence equals the number of words after it 
(ignore the middle word itself if the total count is odd).

Example:
Input: "the quick brown fox jumps"
Output: True
Explanation: 5 words total, "brown" is the middle word, 2 words 
before ("the", "quick") and 2 after ("fox", "jumps") — balanced.

'''

def isBalanced(sentence : str) -> bool :
    if not sentence :
        return False

    list_words = sentence.split()
    size = len(list_words)

    if size % 2 == 0 :
        return False
    

    preCount = 0
    sufixCount = 0
    for idx, word in enumerate(list_words):
        if idx < size // 2 :
            preCount += len(word)
        elif idx > size // 2 :
             sufixCount += len(word)
        else :
            continue 
        
    return preCount == sufixCount


