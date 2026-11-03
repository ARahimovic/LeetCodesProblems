'''
Given a string s, return the character that appears most frequently. 
If multiple characters tie for frequency, return the one that appears first in the original string. 
Ignore whitespaces.
'''

def topRepeatedChar(s : str) -> str :
    if not s :
        return ""

    char_count = {}
    
    for c in s.lower() :
        if not c.isspace() :
            char_count[c] = char_count.get(c, 0) + 1
    

    #return max(char_count, key=char_count.get) if char_count else ""

    max_count = 0
    returnVal = ""
    for key, value in char_count.items() :
        if value > max_count :
            max_count = value
            returnVal = key
    
    return returnVal

assert(topRepeatedChar("hello world") == 'l')
assert(topRepeatedChar(" ") == '')
assert(topRepeatedChar("") == '')
assert(topRepeatedChar("      ") == '')
assert(topRepeatedChar("aaaBBAbb") == 'a')





