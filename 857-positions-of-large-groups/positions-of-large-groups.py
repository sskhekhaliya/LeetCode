class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        stack = [s[0]]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                stack[-1] = stack[-1] + s[i]
            else:
                if len(stack[-1]) < 3:
                    stack.pop()
                stack.append(s[i])

        if len(stack[-1]) < 3:
            stack.pop()
        
        result = []
        for i in stack:
            result.append([s.index(i), s.index(i)+len(i)-1])
            s = s.replace(i, '_'*len(i), 1)

        return result