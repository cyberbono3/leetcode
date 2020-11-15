"""


815. Bus Routes
Hard

911

29

Add to List

Share
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation: 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 10^5.
0 <= routes[i][j] < 10 ^ 6.



"""


from collections import defaultdict, deque

class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        
        [1,2]
        [2,7]
        [7,1]
       
        
        
        [3,6]
        [6,7]
        [7,3]
     
        
        
        build_graph
        
       
       
        
        
        """
        def bfs():
            q = deque()
            q.append((S, 1))
            visited = set()
            while q :
                curr_stop, bus_count = q.popleft()
                
                curr_bus = stop_to_bus[curr_stop]
                
                visited.add(curr_stop)
               
                if curr_stop == T:
                    return bus_count
                
                for next_stop, next_bus in graph[curr_stop]:
                    
                    if next_stop not in visited:
                        if curr_bus != next_bus:
                            q.append((next_stop, bus_count+1))
                        else:
                             q.append((next_stop, bus_count))
            return -1
                        
                    
        graph = defaultdict(set)
        stop_to_bus = {}
        for i,route in enumerate(routes):
            n = len(route)
            for j in range(n):
                graph[route[j]].add((route[(j+1) % n], i))
                stop_to_bus[route[j]] = i
      
        return bfs()
        