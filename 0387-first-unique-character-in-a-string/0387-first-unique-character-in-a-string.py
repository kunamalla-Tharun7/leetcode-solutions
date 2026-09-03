class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for ch in s:
            d[ch]=d.get(ch,0)+1
        for i,ch in enumerate(s):
            if d[ch]==1:
                return i
        return -1