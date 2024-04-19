from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = 0
        seen = set()
        left = 0

        for right, num in enumerate(nums):
            while num in seen:
                current_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            
            seen.add(num)
            current_sum += num
            max_sum = max(max_sum, current_sum)
        
        return max_sum
