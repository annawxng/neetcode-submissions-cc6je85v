class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            if n == 1:
                return True
            visit.add(n)
            n = self.sumOfSquares(n)
        return False


        
    
    # n = 100
    # 1^2 + 0^2 + 0^2
    def sumOfSquares(self, n: int) -> int:
        total = 0
        while n:
            digit = n % 10
            total += digit ** 2
            n = n // 10
        return total

