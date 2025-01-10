class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        def can_break_from_index_to_end(index):
            if index == len(s):
                return True

            if index in memo:
                return memo[index]

            can_break = False

            for i in range(index, len(s)):
                potential_word = s[index : i + 1]

                if potential_word in word_set and can_break_from_index_to_end(i + 1):
                    can_break = True

            memo[index] = can_break
            return memo[index]

        return can_break_from_index_to_end(0)
