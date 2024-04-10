class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        result = -1

        for i in range(len(nums)):
            if i%10 == nums[i]:
                result = i
                break
        
        return result