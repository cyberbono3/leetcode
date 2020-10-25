
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        dic = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            dic[key].append(word)
        return list(dic.values())

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


        
        