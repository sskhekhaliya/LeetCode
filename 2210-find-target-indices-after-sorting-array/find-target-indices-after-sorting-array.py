class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_sorted = sorted(nums)
        return [i for i in range(len(nums)) if nums_sorted[i]==target]
        