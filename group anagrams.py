import collections
class Solution:
    def groupAnagrams(self, strs):
        dic = collections.defaultdict(list)
        for i in strs:
            binary_response = [0] * 26
            for j in i:
                binary_response[ord(j) - ord('a')] += 1
            dic[tuple(binary_response)].append(i)
        return dic.values()