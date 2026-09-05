class Solution:
    def numberOfSteps(self, num: int) -> int:
        count_=0
        while True:
            if num==0:
                return count_
            if num%2==0:
                num//=2
                count_+=1
            else:
                num=num-1
                count_+=1
        return count_