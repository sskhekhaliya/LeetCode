class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        
        for i, row in enumerate(mat):
            if row.count(1) == 1:
                index = row.index(1)
                cols = [row[index] for row in mat]
                if cols.count(1) == 1:
                    count += 1
                    
        return count