#Solution 1
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s :
            return 0

        #remove leading white space
        s = s.lstrip()
        n = len(s)
        str_result = ""
        foundDigit = False
        MAX_SIGNED_INT_32 = 2**31 - 1
        MIN_SIGNED_INT_32 = -2**31

        for i,ch in enumerate(s):
            if ch.isdigit():
                foundDigit = True
                str_result += ch
            else: # a non digit charachter
                if foundDigit : #we already found a digit and current ch is not a digit, so break imediatly
                    break
                elif (i+1)<n and s[i+1].isdigit() and (ch == '-' or ch == '+'):   
                    str_result += ch
                else: # we didnt find a digit and current char is not a digit
                    return 0

        result = int(str_result) if str_result else 0
        if result > MAX_SIGNED_INT_32 :
            result = MAX_SIGNED_INT_32
        elif result < MIN_SIGNED_INT_32 :
            result = MIN_SIGNED_INT_32
        
        return result

#Solution 2

class Solution:
    def myAtoi(self, s: str) -> int:
        #remove leading white space
        s = s.lstrip()

        if not s :
            return 0

        n = len(s)
        index, sign = 0,1
        result = 0
        MAX_SIGNED_INT_32 = 2**31 -1
        MIN_SIGNED_INT_32 = - 2**31

        if s[index] in ('+','-'):
            sign = 1 if s[index] == '+' else -1
            index += 1
        
        while index < n and s[index].isdigit():
            result = result * 10 + ord(s[index]) - ord('0')
            index +=1
        
        result *= sign
        

        if result > MAX_SIGNED_INT_32 :
            result = MAX_SIGNED_INT_32
        elif result < MIN_SIGNED_INT_32:
            result = MIN_SIGNED_INT_32
        
        return result
