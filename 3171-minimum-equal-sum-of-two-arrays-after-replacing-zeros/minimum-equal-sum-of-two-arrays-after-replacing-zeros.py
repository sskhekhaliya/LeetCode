class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        min_nums1_sum = sum([1 if x==0 else x for x in nums1])
        min_nums2_sum = sum([1 if x==0 else x for x in nums2])
        
        if (nums1.count(0) == 0 and min_nums1_sum < min_nums2_sum) or (nums2.count(0) == 0 and min_nums2_sum < min_nums1_sum):
            return -1
        else:
            return max(min_nums1_sum, min_nums2_sum)
