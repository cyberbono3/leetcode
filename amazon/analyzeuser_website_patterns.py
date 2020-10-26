
from collections import defaultdict


from itertools import combinations

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        
        
        Example 1:

        Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
        Output: ["home","about","career"]
        Explanation: 
        The tuples in this example are:
        ["joe", 1, "home"]
        ["joe", 2, "about"]
        ["joe", 3, "career"]
        ["james", 4, "home"]
        ["james", 5, "cart"]
        ["james", 6, "maps"]
        ["james", 7, "home"]
        ["mary", 8, "home"]
        ["mary", 9, "about"]
        ["mary", 10, "career"]
        The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
        The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
        The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
        The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
        The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
        
        
        dic = {}
        
        for u,t,w in zip(username, timestamp, website):
            dic[(w,t)] += 1
        
        
        
        
        """
        
        packed_tuple = zip(timestamp,username, website)  # # ---> [(3, 'joe', 'career'),....]
        sorted_packed_tuple = sorted(packed_tuple, key = lambda x: x[0])
        
        mapping = defaultdict(list)
        
        for _,u,w in sorted_packed_tuple:   # joe:[home, about , career]
            mapping[u].append(w)
        print(mapping)
        #defaultdict(<type 'list'>, {u'james': [u'home', u'cart', u'maps', u'home'], u'joe': [u'home',          #u'about', u'career'], u'mary': [u'home', u'about', u'career']})

            
        count_dic = defaultdict(int)
        for website_list in mapping.values():
            combs = set(combinations(website_list, 3))
            for comb in combs:
                count_dic[comb] += 1
        print(count_dic)
        return sorted(count_dic.items(), key = lambda x:(-x[1], x[0]))[0][0]