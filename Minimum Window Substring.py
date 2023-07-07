# My solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):
            return ""
        dic = {}
        lis = []
        min_string = s
        current_string = ""
        R = 0
        flag = False
        first = True

        for i in t:
            dic[i] = 1 + dic.get(i, 0)

        while R < len(s):
            if s[R] in dic.keys():
                if first == True:
                    L = R
                    first = False
                lis.insert(0, R)
                dic[s[R]] = dic.get(s[R]) - 1
                if max(dic.values()) <= 0:
                    flag = True
                    current_string = s[L:R+1]
                    min_string = current_string if len(current_string) < len(min_string) else min_string
                    dic[s[lis[-1]]] = dic.get(s[lis[-1]]) + 1
                    lis.pop()
                    L = 0 if len(lis) == 0 else lis[-1]
                    dic[s[R]] = dic.get(s[R]) + 1
                    R = R - 1
                    if len(lis) != 0:
                        del lis[0]

            R += 1
        return "" if flag == False else min_string

# Actual solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
