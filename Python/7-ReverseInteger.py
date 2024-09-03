class Solution:
    def reverse(self, x: int) -> int:
        if abs(x)< 10:
            return x
        
        MAX_SIGNED_INT_32 = 2**31 - 1
        MIN_SIGNED_INT_32 = -2**31
        sign = 1
        s = str(x)

        if s[0] in ('+', '-'):
            sign = 1 if s[0] == '+' else -1
            s = s[0] + s[-1:0:-1]
        else:
            s = s[::-1]

        result = int(s)
        if result > MAX_SIGNED_INT_32 or result < MIN_SIGNED_INT_32:
            return 0
        return result