class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        min_operations = float('inf')

        for i in range(n + 1):
            for j in range(i, n + 1):
                changes = sum(1 for num in nums[:i] if num != 1) + \
                          sum(1 for num in nums[i:j] if num != 2) + \
                          sum(1 for num in nums[j:] if num != 3)
                min_operations = min(min_operations, changes)

        return min_operations
