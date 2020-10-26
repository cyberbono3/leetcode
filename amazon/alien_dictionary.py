"""
269. Alien Dictionary
Hard

2043

392

Add to List

Share
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".
Note:

You may assume all letters are in lowercase.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.




"""

from collections import defaultdict, deque



class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        
        
        Input:
        [
        "wrt",
        "wrf",
        
        "er",
        "ett",
        "rftt"
]
        t -> f
        w -> e
        r -> t
        e -> r
        t -> f
        
        
        
        """
        def build_graph(first, second):
            first_len, second_len = len(first), len(second)
            min_len = min(first_len, second_len)
            for i in range(min_len):
                if first[i] == second[i]:
                    continue
                u, v = first[i], second[i]
                if v not in graph[u]:
                    graph[u].add(v)
                    indegree[u] = indegree.get(u, 0)
                    indegree[v] = indegree.get(v, 0) + 1
                
            

        
        # find  itme with indegree = 0
        def top_ordering(start):
            q = deque(start)
            res = ""
            visited = set()
            while q:
                curr = q.popleft()
                res += curr
                for nei in graph[curr]:
                    indegree[nei] -= 1
                    if not indegree[nei]:
                        q.append(nei)
                    
            return res if len(res) == len(indegree)  else ""
                
                
            
                
        def find_start_vertex():
            return [k for k,v in indegree.items() if not v]
            
    
        
        graph = defaultdict(set)
        indegree = {}
        for i in range(1, len(words)):
            build_graph(words[i-1], words[i])
        start  = find_start_vertex()
        return top_ordering(start)