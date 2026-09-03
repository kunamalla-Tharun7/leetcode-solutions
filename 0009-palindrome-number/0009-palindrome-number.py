class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num=x
        reversed_num=0
        while num>0:
            last_digit=num%10
            reversed_num=reversed_num*10+last_digit
            num//=10
        if x==reversed_num:
            return True
        return False