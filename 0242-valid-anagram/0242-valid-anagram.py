class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        for ch in s:
            d[ch]=d.get(ch,0)+1
        for ch in t:
            d[ch]=d.get(ch,0)-1
        res=all(value==0 for value in d.values())
        return res