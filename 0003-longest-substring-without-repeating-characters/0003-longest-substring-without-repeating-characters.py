class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        d={}
        maxi=0
        while r<len(s):
            if s[r] in d:
                l=max(l,d[s[r]]+1)
            d[s[r]]=r
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi