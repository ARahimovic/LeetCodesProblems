
# def room_intervals(intervals : list[list]) -> bool :
#     if not intervals :
#         return False 
    
#     if len(intervals) == 1 :
#         return True
    

#     intervals.sort()
#     last  = intervals[0]

#     for interval in intervals[1:] :
#         if interval[0] < last[1] :
#             return False
        
#         last = interval
    
#     return True


# a = [[0, 30], [5, 10], [15, 20]]
# b = [[7, 10], [2, 4]]
# c = [] 
# d = [[4,5]]


# assert room_intervals(a) == False
# assert room_intervals(b) == True
# assert room_intervals(c) == False
# assert room_intervals(d) == True


'''
Mockup 3: Balanced Parsing & Dynamic Programming (Medium Spike)
Focus: Stack structures, state memoization, prefix validation.
Problem 1: Balanced Brackets with Custom Pairs
Given a string containing characters (), [], {} alongside other characters, determine if the bracket ordering is strictly valid.
Sample Input: "{ [ ( a + b ) * c ] }"
Expected Output: true
Sample Input: "([)]"
Expected Output: false
Key Consideration: Stack-based matching. Ensure edge cases like trailing open brackets (e.g., "(((") or closing brackets with empty stacks are handle
'''


from collections import deque
def is_balanced(s : str) -> bool :
    if not s :
        return True

    stack = deque()

    parentheses_map = {'}': '{' , ')' :'(' , ']' : '['}

    for ch in s :
        if ch in parentheses_map.values() :
            stack.append(ch)
        
        elif ch in parentheses_map :
            if not stack or  stack.pop() != parentheses_map[ch]:
                return False
            
    return len(stack) == 0


if __name__ == "__main__" :
    a = "{ [ ( a + b ) * c ] }"
    assert is_balanced(a) == True
    b = "([)]"
    assert is_balanced(b) == False

        
            
    

