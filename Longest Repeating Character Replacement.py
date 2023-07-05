#My sol
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic={}
        result= 0
        L, R = 0, 0
        while R<len(s):
            dic[s[R]] = 1 + dic.get(s[R], 0)
            if R-L+1-max(dic.values()) <= k:
                result = max(result, R-L+1)
                R = R + 1
            else:
                dic[s[L]] = dic.get(s[L]) - 1
                L = L + 1
                dic[s[R]] = dic.get(s[R]) - 1
        return result

#Actual Solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic={}
        result= 0
        L = 0
        for R in range(len(s)):
            dic[s[R]] = 1 + dic.get(s[R], 0)
            if R - L + 1 - max(dic.values()) > k:
                dic[s[L]] = dic.get(s[L]) - 1
                L = L + 1
            result = max(result, R-L+1)
        return result