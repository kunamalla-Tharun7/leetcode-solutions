class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        l=0
        r=len(nums)-1
        k=len(nums)-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                res[k]=nums[l]**2
                l+=1
                k-=1
            else:
                res[k]=nums[r]**2
                r-=1
                k-=1
        return res