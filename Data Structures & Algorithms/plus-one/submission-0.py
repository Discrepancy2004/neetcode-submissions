class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = [1]
        for num in range(len(digits)-1,-1,-1):

            if digits[num] != 9:
                digits[num] += 1
                return digits
            
            digits[num] = 0
        
        arr.extend(digits)
        return arr