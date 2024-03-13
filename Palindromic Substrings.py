class Solution:
    def countSubstrings(self, s: str) -> int:

        result = 0
        for i in range(len(s)):
            # if odd
            L, R = i, i
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    result = result + 1
                    L = L - 1
                    R = R + 1
                else:
                    break
            # if eve
            L, R = i, i + 1
            while L >= 0 and R < len(s):
                if s[L] == s[R]:
                    result = result + 1
                    L = L - 1
                    R = R + 1
                else:
                    break
        return result