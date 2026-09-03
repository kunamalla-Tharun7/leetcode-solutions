class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        original=x
        sum_=0
        while x>0:
            last_digit=x%10
            sum_+=last_digit
            x//=10
        if original %sum_==0:
            return sum_
        return -1