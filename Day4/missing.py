def missing(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            if nums[i] == nums[v - 1]:
                break
    print("Second")
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1

print(missing([1,2,4]))