class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute force
        ans = []
        i = 0
        while i < len(nums):
            if target - nums[i] in nums and nums.index(target - nums[i]) != i:
                ans.append(i)
                ans.append(nums.index(target - nums[i]))
                return sorted(ans)
            i += 1