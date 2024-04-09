class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        stack = []
        words_len = len(words)

        for i in range(words_len):
            for j in range(words_len):
                if j != i and words[i] in words[j]:
                    stack.append(words[i])
                    break
        
        return stack