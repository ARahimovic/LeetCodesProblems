'''
Given a paragraph of text and a list of banned words, return the 
most frequent word that is NOT in the banned list. Words are 
case-insensitive, and punctuation should not be considered part 
of a word.

Example:
Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: "hit" occurs 3 times but is banned. "ball" occurs 2 times 
and is the most frequent non-banned word.

'''


def mostCommonWord(paragraph : str, banned : list[str]) -> str :
    if not paragraph :
        return ""
    
    banned_set = set(banned)
    word_count = {}

    stripped_paragraph = "".join(ch.lower() if ch.isalnum() else " " for ch in paragraph)
    for word in stripped_paragraph.split() :
        if word in banned_set :
            continue
        
        word_count[word] = word_count.get(word, 0) + 1
    
    return max(word_count, key=word_count.get) if word_count else "".


assert(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]) == "ball")