#My Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = list(s)
        l2 = list(t)
        dic1 = {}
        dic2 = {}

        for i in l1:
            flag = 0
            try:
                x = dic1[i]
            except:
                flag = 1

            if flag == 1:
                dic1[i] = 1
            else:
                dic1[i] = dic1[i]+1

        for i in l2:
            flag = 0
            try:
                x = dic2[i]
            except:
                flag = 1

            if flag == 1:
                dic2[i] = 1
            else:
                dic2[i] = dic2[i]+1

        if dic1 == dic2:
            return True
        else:
            return False

#Refered Solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dicS, dicT= {}, {}
        for i in range(len(s)):
            dicS[s[i]] = 1 + dicS.get(s[i],0)
            dicT[t[i]] = 1 + dicT.get(t[i],0)

        return dicS==dicT