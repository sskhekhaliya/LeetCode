class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f_nos = [1, 1]

        while f_nos[-1]+f_nos[-2] <= k:
            f_nos.append(f_nos[-1]+f_nos[-2])
        
        count = 0
        for num in reversed(f_nos):
            if k >= num:
                k -= num
                count += 1
            if k == 0:
                break
        
        return count