class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        idx = len(nums) - 1
        left = 0
        right = len(nums) - 1
        ans = [0] * len(nums)

        while left <= right:
            left_sum = nums[left]**2
            right_sum = nums[right]**2

            if left_sum > right_sum:
                ans[idx] = left_sum
                left+=1
            else:
                ans[idx] = right_sum
                right-=1
            idx = idx - 1

        return ans