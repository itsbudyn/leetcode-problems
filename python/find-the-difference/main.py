class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = {}
        
        for i in set(s):
            s_dict[i] = s.count(i)
        for i in set(t):
            if i not in s_dict.keys() or s_dict[i] != t.count(i): return i