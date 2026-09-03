class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            total=0
            if n in seen:
                return False
            seen.add(n)
            while n >0:
                last_digit=n%10
                total+=last_digit**2
                n//=10
            n=total
        return True