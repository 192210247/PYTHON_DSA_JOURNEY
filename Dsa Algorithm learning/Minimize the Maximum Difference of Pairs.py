def minimizeMax(nums, p):
    nums.sort()

    def can_form_pairs(D):
        count = 0
        i = 0
        n = len(nums)
        while i < n - 1:
            if nums[i + 1] - nums[i] <= D:
                count += 1
                i += 2 
            else:
                i += 1 
        return count >= p

    left = 0
    right = nums[-1] - nums[0]  
    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_form_pairs(mid):
            answer = mid
            right = mid - 1  
        else:
            left = mid + 1  

    return answer
nums = [1, 3, 6, 19, 20]
p = 2
print(minimizeMax(nums, p))