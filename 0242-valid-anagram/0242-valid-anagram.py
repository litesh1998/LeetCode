from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_set = set(s)
        t_set = set(t)

        if t_set!=s_set:
            return False

        d= defaultdict(int)
        for i in s:
            d[i]+=1

        for i in t:
            d[i]-=1

        for i in d.values():
            if i !=0:
                return False
        return True  