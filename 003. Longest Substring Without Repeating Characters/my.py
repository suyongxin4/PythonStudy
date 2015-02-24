class Solution:
    # @return an integer
    # def lengthOfLongestSubstring(self, s):
    #     length = len(s)
    #     if length == 0:
    #         return 0
    #     cache = list(map(lambda x: None, range(length)))
    #     for i in range(len(s)):
    #         if i == 0:
    #             cache[i] = 1
    #             continue
    #         else:
    #             cache[i] = cache[i - 1];
    #             if self._isUniqueString(s[i - cache[i - 1]:i+1]):
    #                 cache[i] += 1
    #     return cache[length - 1]

    # def _isUniqueString(self, s):
    #     setCache = set()
    #     for c in s:
    #         if c in setCache:
    #             return False
    #         else:
    #             setCache.add(c)
    #     return True

    def lengthOfLongestSubstring(self, s):
        cDic = {}
        start = result = 0
        for i, c in enumerate(s):
            if c in cDic and cDic[c] >= start:
                start = cDic[c] + 1
            else:
                result = max(result, i - start + 1)
            cDic[c] = i
        return result