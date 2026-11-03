'''
Given two strings a and b of equal length, return the minimum number of character swaps/replacements needed to transform a into an anagram of b.

Sample Input: a = "night", b = "thing"
Expected Output: 0 (they are already anagrams)

Sample Input: a = "apple", b = "apply"
Expected Output: 1 (replace 'e' with 'y')
'''

######################
def min_num_anagram(a :str, b :str) -> int :
    if not a or not b or len(a) != len(b):
        return -1

    word_count_a = {}
    word_count_b = {}

    for idx in range(len(a)) :
        word_count_a[a[idx]] = word_count_a.get(a[idx], 0) + 1
        word_count_b[b[idx]] = word_count_b.get(b[idx], 0) + 1

    diff = 0
    for char, count in word_count_a.items() :
        if count > word_count_b.get(char, 0) :
            diff += count - word_count_b.get(char, 0)

    return diff




assert min_num_anagram("night", "thing") == 0
assert min_num_anagram("apple", "apply") == 1



### using counter

from collections import Counter
def min_num_anagram(a :str, b :str) -> int :
    if not a or not b or len(a) != len(b):
        return -1

    count_a = Counter(a)
    count_b = Counter(b)

    diff_count = 0
    for char, count in count_a.items() :
        if count > count_b[char] :
            diff_count += count - count_b[char]
    
    return diff_count
