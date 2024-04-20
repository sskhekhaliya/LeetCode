class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        count = 0
        
        for sublist in nums:
            sublist.sort(reverse=True)
        
        for i in range(len(nums[0])):
            count += max(row[i] for row in nums)
        
        return count