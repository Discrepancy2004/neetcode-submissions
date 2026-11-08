class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        total = n
        digits = str(n)
        while(total != 1 and total not in seen):
            seen.add(total)
            total = 0
           
            for digit in digits:
                num = int(digit)
                total += num * num
            
            digits = str(total)
            
        return total == 1

        
        