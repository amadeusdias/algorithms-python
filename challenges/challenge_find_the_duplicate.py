def find_duplicate(nums):
    nums.sort()
    if not nums or len(nums) == 1:
        return False
    nlist = set()
    for i, n in enumerate(nums):
        if not isinstance(n, int) or n < 0:
            return False
        if n in nlist:
            return n
        nlist.add(n)
    return False
