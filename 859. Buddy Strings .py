class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            seen = set()
            for char in s:
                if char in seen:
                    return True
                seen.add(char)
            return False

        diffs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diffs.append((s[i], goal[i]))

        if len(diffs) == 2 and diffs[0] == diffs[1][::-1]:
            return True

        return False
