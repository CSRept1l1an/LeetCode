class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = ''.join(sorted(t))
        s = ''.join(sorted(s))
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]

        return t[len(s)]