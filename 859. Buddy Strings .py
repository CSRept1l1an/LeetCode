
def buddyStrings(self, s: str, goal: str) -> bool:
    changes = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            changes.append(s[i])
            changes.append(goal[i])

    if changes == changes[::-1]:
        return True


