class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        char_map = {}
        word_map = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in char_map:
                if char_map[char] != word:
                    return False
            else:
                char_map[char] = word

            if word in word_map:
                if word_map[word] != char:
                    return False
            else:
                word_map[word] = char

        return True