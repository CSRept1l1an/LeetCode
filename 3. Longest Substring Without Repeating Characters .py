def lengthOfLongestSubstring(s: str) -> int:
    charlist = {}
    first = 0
    longest = 0
    for i, char in enumerate(s):
        if char in charlist and charlist[char] >= first:
            first = charlist[char] + 1
        charlist[char] = i

        longest = max(longest, i - first + 1)

    return longest


st = "abcabcbb"
print(lengthOfLongestSubstring(st))
