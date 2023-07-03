#My Solution 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R = 0, 0
        maxLen = 0
        lis = []
        while R < len(s):
            if s[R] not in lis:
                lis.append(s[R])
                maxLen = max(maxLen, len(lis))
                R += 1
            else:
                lis.clear()
                L += 1
                R = L
        return maxLen

#My Solution 2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R = 0, 0
        maxLen = 0
        lis = []
        while R < len(s):
            if s[R] not in lis:
                lis.append(s[R])
                maxLen = max(maxLen, len(lis))
                R += 1
            else:
                lis.remove(s[L])
                L = L + 1
        return maxLen

#Opt Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
