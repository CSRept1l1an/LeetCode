class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]

        return t[len(s)]