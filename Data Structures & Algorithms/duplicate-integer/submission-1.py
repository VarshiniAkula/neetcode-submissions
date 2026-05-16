class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set(nums)
        l1 = len(a)
        l2 = len(nums)
        if l1 == l2:
            return False
        else:
            return True


        