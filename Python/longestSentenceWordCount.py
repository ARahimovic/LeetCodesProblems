'''
You're given a string of text containing words, spaces, and 
sentence-ending punctuation (., !, ?). Sentences are separated by 
one of these punctuation marks. Return the maximum number of words 
found in any single sentence.

Words are separated by one or more spaces. Assume punctuation only 
appears at the end of a sentence, not inside a word.

Example:
Input: "Hello there, friend. How are you doing today? I am fine!"
Output: 5
Explanation: "How are you doing today" has 5 words, which is the max 
across all three sentences.
'''

def longestSentence(paragraph : str) -> int :
    if not paragraph :
        return 0
    
    punctation = {'.', '!', "?"}

    stripped = "".join("." if ch in punctation else ch for ch in paragraph)
    list_sentences = stripped.split('.')

    max_size = 0
    for sentence in list_sentences :
        max_size = max(len(sentence.split()), max_size)
    
    return max_size


print(longestSentence("Hello there, friend. How are you doing today? I am fine!"))
