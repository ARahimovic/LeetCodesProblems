def threeSum(nums) :
    nums.sort()
    result = set()

    for i in range(len(nums)) :
        left = i + 1
        right = len(nums) - 1
        while left <= right :
            if nums[left] + nums[right] == -nums[i] :
                result.add(tuple(sorted(nums[left] + nums[right], nums[i])))
                break
            elif nums[left] + nums[right] < -nums[i] :
                left += 1
            else :
                right -= 1

    return result     