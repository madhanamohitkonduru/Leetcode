#Case 1
# s1 = "ab"
# s2 = "eidbaooo"
#
# Case 2
# s1 = "ab"
# s2 = "eidboaoo"

# mY sol

dic = {}
size = len(s1)
for i in s1:
    dic[i] = 1 + dic.get(i, 0)
i = 0
while i < len(s2):
    print(i)
    if s2[i] in dic.keys():
        L = i
        R = i + size
        print(L, R)
        dic2 = dic.copy()
        for j in range(L, R, 1):
            print("for", j)
            if dic2[s2[j]] != 0:
                dic2[s2[j]] = dic2[s2[j]] - 1
            else:
                break
            if max(dic2.values()) == 0:
                print(True)

    i = i + 1
print(False)

#Opt sol
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
