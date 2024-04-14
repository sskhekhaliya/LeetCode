class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        max_occurrence = max(char_count.values())

        max_occ_chars = {char for char, count in char_count.items() if count == max_occurrence}

        s = ''.join(char for char in s if char in max_occ_chars)

        result = ""
        while len(s) > 0:
            result = s[-1] + result
            s = s.replace(s[-1], '')
        
        return result
