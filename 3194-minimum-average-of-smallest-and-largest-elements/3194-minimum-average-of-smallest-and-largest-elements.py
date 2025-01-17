class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()

        left = 0
        right = len(nums) - 1
        idx = len(nums)/2
        ans = []

        while left < right and idx > 0:
            avg = (nums[left] + nums[right])/2
            ans.append(avg)
            idx -= 1
            left += 1
            right -= 1
        
        ans.sort()
        
        return ans[0]
