class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elmap = {}
        longest = 0

        for num in nums:
            elmap[num] = True
        
        for key in elmap:
            if (key - 1) in elmap:
                elmap[key] = False
        

        for key in elmap:
            if elmap[key] == True:
                temp_len = 0
                cur = key
                while cur in elmap:
                    temp_len+=1
                    cur+=1
                
                if temp_len > longest:
                    longest = temp_len
        

        return longest


