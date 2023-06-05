# def find_duplicate(nums):
#    if not nums:
#        return False
#    if len(nums) == 1:
#        return False
#    for i, n in enumerate(nums):
#        if not isinstance(n, int):
#            return False
#        elif n < 0:
#            return False
#        elif n == nums[i+1]:
#            return n
#        else: return False
