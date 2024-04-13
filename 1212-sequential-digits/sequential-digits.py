class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        low_len = len(str(low))
        first_num = ''

        for i in range(1, low_len+1):
            first_num += str(i)

        first_num = int(first_num)
        

        while first_num <= high and len(str(first_num)) < 9:
            if str(first_num)[-1] == '0':
                first_num = int(''.join(str(i) for i in range(1, low_len+2)))
                low_len += 1
            if first_num >= low and first_num <= high:
                result.append(first_num)
            first_num += int('1'*low_len)
            
        
        return result


