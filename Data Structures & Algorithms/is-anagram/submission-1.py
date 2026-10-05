class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s = sorted(s)
            t = sorted(t)
            return s==t
        else:
            return False
