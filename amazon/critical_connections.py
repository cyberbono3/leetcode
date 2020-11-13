"""

https://leetcode.com/problems/critical-connections-in-a-network/

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.


Bruteforce
class Solution:
    def criticalConnections(self, n, connections):
        if not n or not connections : return []
        
        
        def dfs(edges, visited):
            for u,v in edges:
                visited.add(u)
                visited.add(v)
            return len(visited) == n
        
        res = []
  
        for i,conn  in enumerate(connections):
            edges = connections[:i]  + connections[i+1:]
            if not dfs(edges, set()):
                res.append(conn)
                break
        return res
    
sol = Solution()
print(sol.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]) == [[1,3]])



"""


        
import collections

class Solution:
    def criticalConnections(self, n, connections) :
        def dfs(rank, curr, prev):
            low[curr], result = rank, []
            for neighbor in graph[curr]:
                if neighbor == prev: continue
                if not low[neighbor]:
                    result += dfs(rank + 1, neighbor, curr)
                low[curr] = min(low[curr], low[neighbor])
                if low[neighbor] >= rank + 1:
                    result.append([curr, neighbor])
            print(low)
            return result

        low, graph = [0] * (n+1), collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        return dfs(1, 1, 1)