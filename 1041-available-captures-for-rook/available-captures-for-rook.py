class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        R_pos = None
        B_pos = []
        p_pos = []

        for i, cols in enumerate(board): #i: row, j: col
            for j, chessman in enumerate(cols):
                if chessman == 'R':
                    R_pos = (i+1, j+1)
                if chessman == 'B':
                    B_pos.append((i+1, j+1))
                if chessman == 'p':
                    p_pos.append((i+1, j+1))

        count = 0

        i, j = R_pos
        #horizontally moving
        for x in range(j - 1, 0, -1):
            if (i, x) in B_pos or (i, x) in p_pos:
                if (i, x) in p_pos:
                    count += 1
                break
        
        for x in range(j+1, 9):
            if (i, x) in B_pos or (i, x) in p_pos:
                if (i, x) in p_pos:
                    count += 1
                break
        
        #vertically moving
        for x in range(i - 1, 0, -1):
            if (x, j) in B_pos or (x, j) in p_pos:
                if (x, j) in p_pos:
                    count += 1
                break
        
        for x in range(i+1, 9):
            if (x, j) in B_pos or (x, j) in p_pos:
                if (x, j) in p_pos:
                    count += 1
                break

        return count