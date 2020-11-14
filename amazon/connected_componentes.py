class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        
        
        Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]
        
        #i=0..4
      
    
    
        
        
        
        
        
        """
        
        def dfs(v, visited):
            stack = [v]
            while stack:
                curr = stack.pop()
                visited.add(curr)
                for nei in graph[curr]:
                    if nei not in visited:
                        stack.append(nei)
                
            
        
        
        
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        count = 0
        visited = set()
        for i in range(n):
            if i not in visited and len(visited) < n:
                dfs(i, visited)
                count += 1
        return count
        
       