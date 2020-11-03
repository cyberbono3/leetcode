# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        
        
        3 people
        
        
        edge cases:
        2 <= n <= 100
        
        
        indegree = {}
        outdegree = {}
        
        O(n^2)
        
        
        for loop i from 0 to 2(including)
            for loop j from 1 up 3
                    conn =  knows(i,j)
                    if conn:
                        increment indegree j
                        increment outdegree i
                    conn = knolws(j,i)
                    if conn:
                        increment indegree i
                        increment outdegree j
        
        we find vertrex with outdegree == 0
        oif there is no such vertex then we output -1
        if there is such vertex thenwe check if indegree[v]  == n-1 if it output this vertex othwerwise -1
    
        0 1 2 
          i j
        
        (0,1) knows true
        (0,2)  knwoes true
        (1,2) knolwes true
        outptu 2 cause indegree[2] == 2(n-1) and outdegree[2]  == 0
        
        
        (0,1)
        (1,2)
        (2,0)  output -1
        
        
        
        3
        
        0,1,2
          i 
        j 
        
        """
       
        outdegree = {}
        indegree = {}
        
        # preprocessing phase
        for i in range(n):
            outdegree[i] = 0
            indegree[i] = 0
    
         # we check every pair of dicints values
        for i in range(n):
            for j in range(n):
                if i == j :
                    continue
                if knows(i, j):
                    outdegree[i] += 1
                    indegree[j] += 1
      
    
        for i in range(n):
            if not outdegree[i] and indegree[i] == n-1:
                return i
        return -1
    
    
    
    
    """
    
     
        cand = 0
        for i in range(n):
            # if all vertexes are incoming to candidate then
            if knows(cand, i):
                cand = i
        print(cand)
                
        #if there are some outdgoing edges return -1
        if any(knows(cand, i) for i in range(cand)):
            return -1
        
        if any(not knows(i,cand) for i in range(n)):
            return -1
        
        return cand
    
    
    
    
    
    
    
    """
        