class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_num = min(len(word1), len(word2))
        res = ''

        for i in range(min_num):
            res = res + word1[i] + word2[i]

        if min_num == len(word1):
            for i in range(min_num, len(word2)):
                res += word2[i]
        else:
            for i in range(min_num, len(word1)):
                res += word1[i]

        return res