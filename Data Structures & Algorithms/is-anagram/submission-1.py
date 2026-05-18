class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = Counter(s)
        t1 = Counter(t)

        if s1==t1:
            return True
        else:
            return False
        

            

            

