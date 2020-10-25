



from collections import deque


class TrieNode:
    def __init__(self):
        self.leaves = {}
        self.end_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.trie = TrieNode()
        
    def insert(self, word):
        curr = self.trie
        for ch in word:
            if ch not in curr.leaves:
                curr.leaves[ch] = TrieNode()
            curr = curr.leaves[ch]
        
        curr.end_word = True
        curr.word = word
    
    def neighbours(self, r, c, visited, board):
        R, C = len(board), len(board[0])
        for nr,nc in ((r+1,c), (r-1,c), (r, c+1), (r,c-1)):
            if 0 <= nr < R and 0 <= nc < C and (nr,nc) not in visited:
                yield(nr,nc)
        
    def search(self, r, c, board):
        visited = set()
        
        q = deque()
        
        q.append((board[r][c], r, c))

        curr = self.trie
        
        while q:
            char,r,c = q.popleft()
            
            visited.add((r,c))
            
            curr = curr.leaves[char]
            
            if curr.end_word:
                return curr.word
            
            for (nr,nc) in self.neighbours(r,c,visited, board):
                if board[nr][nc] in curr.leaves:
                    q.append((board[nr][nc], nr, nc))
        return ""
               
            
            
    

class Solution(object):
    
    def findWords(self, board, words):
        
        """
        
        brtuteforce approach use bfs
        loop over rows and columns on th board  O(R*C)
          as soon awe hit beginign chrater of any word from words
               we we do bfs to traverse word to find out if we can traverse it  O(v+e) v is number of characters in word
               
        overall space O(R*C * (V+E))    
        
        
        use trie data structure
           we insert all the words in our trie data stcutee   O(n*l)   n is number of words, l max length of the word
            
            class TrieNode:
                 leaves,
                 is_word 
            Trie
               insert
               search
               
        we loop over row and cols:
            after we hit beginning of every wordfrom words
                  search_trie data strutee we can explore all the noighbors in a board tocan advance out pountet
                  
                  we explore al lnerighbours in a board
                  o
               -  a
                  t
                  h
                  is.word = True
                  we add it to the output
               
        
        
        """
        t = Trie()
        for word in words:
            t.insert(word)
            
        
        result = []
        
        R, C = len(board), len(board[0])
        
        for r in range(R):
            for c in range(C):
                if board[r][c] in t.trie.leaves :
                    word = t.search(r,c, board)
                    if word:
                        result.append(word)
        return result
        
        
        