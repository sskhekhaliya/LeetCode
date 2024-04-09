class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        stack = []
        
        for i in nums:
            if i%2==0:
                stack.insert(0, i)
            else:
                stack.append(i)
        
        return stack