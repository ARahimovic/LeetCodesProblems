'''
Given a string, remove duplicate letters so each letter appears only 
once, keeping the first occurrence's position (simplest version — 
there's a much harder LeetCode variant requiring lexicographically 
smallest result + stack, but this simple version is more likely 
in a general screen).

'''

def remove_duplicates(s : str) -> str :
    if not s :
        return ""
    

    seen = set()
    result = []

    for c in s :
        if c in seen :
            continue

        seen.add(c)
        result.append(c)
    
    return "".join(result)


assert remove_duplicates("programming") == "progamin"


'''

Given a sorted array, remove duplicates in-place so each element 
appears only once, and return the new length. Must be done with 
O(1) extra space (modify the array in-place).

Example:
Input: [1,1,2,2,3]
Output: 3, array becomes [1,2,3,_,_]

'''

def remove_duplicates_in_array(nums : list[int]) -> int:
    seen = set()
    write = 0

    for read in range(len(nums)) :
        if nums[read] in seen :
            continue

        seen.add(nums[read])
        nums[write] = nums[read]
        write +=1
    
    return write
        

def remove_duplicates_in_sorted_array(nums : list[int]) -> int:
    write = 1

    
    for read in range(1, len(nums)) :
        if nums[read] == nums[write - 1] :
            continue 
        
        nums[write] = nums[read]
        write += 1
    


def find_first_unique_char(s : str) -> str :
    if not s :
        return -1
    
    char_count = {}
    for c in s :
        char_count[c] = char_count.get(c, 0) + 1
    
    for i,c in enumerate(s) :
        if char_count[c] == 1 :
            return i

   
    return -1
        

def find_first_duplicate_index(nums : list[int]) :

    seen = set()

    num_idx = {}

    for idx, num in enumerate(nums) :
        if num in count_id :
            return count_id(num)

        num_idx[num] = idx

    return None
