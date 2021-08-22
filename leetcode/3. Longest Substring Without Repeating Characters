class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        j = 0
        for i in range(0, len(s)):
            if s[i] in dic:
                j = max(j, dic[s[i]] + 1)

            res = max(res, i - j + 1)
            dic[s[i]] = i

        return res
