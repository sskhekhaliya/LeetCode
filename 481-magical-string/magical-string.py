class Solution:
    def magicalString(self, n: int) -> int:
        s = "122"
        i = 2
        while len(s) < n:
            if s[-1] == '1':
                s += '2'*int(s[i])
            else:
                s += '1'*int(s[i])
            i += 1

        return s[:n].count('1')