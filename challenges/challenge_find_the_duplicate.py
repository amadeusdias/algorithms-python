def find_duplicate(nums):
    nums.sort()
    if not nums:
        return False
    if len(nums) == 1:
       return False
    for i, n in enumerate(nums):
        if not isinstance(n, int) or n < 0:
            return False
        if n in nums[i + 1:]:
            return n
    return False
