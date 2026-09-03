class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_d={}
        t_d={}
        for i in range(len(s)):
            char_s=s[i]
            char_t=t[i]
            if char_s in s_d:
                if s_d[char_s]!=char_t:
                    return False
            if char_t in t_d:
                if t_d[char_t]!=char_s:
                    return False      
            s_d[char_s]=char_t
            t_d[char_t]=char_s
        return True