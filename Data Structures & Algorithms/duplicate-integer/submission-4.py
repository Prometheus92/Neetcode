class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for i in sorted(nums):
            if i in seen:
                return True
            seen.append(i)
        return False