class TrieNode:
    def __init__(self):
        self.leaves = {}
        self.end_of_word = False
    
    


class WordDictionary(object):
    

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()
        
        
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        curr = self.trie
        for ch in word:
            # if the re is no such nodes in a Trie
            if ch not in curr.leaves:
                curr.leaves[ch] = TrieNode()
            curr = curr.leaves[ch]
        curr.end_of_word = True
                
        
    
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        curr = self.trie
        return self.dfs(word, curr)
    
    def dfs(self, word, curr):
        for i, ch in enumerate(word):
            if ch != "." and ch not in curr.leaves:
                return False
            if ch in curr.leaves:
                return self.dfs(word[i+1:], curr.leaves[ch])
            elif ch == "." :
                for k in curr.leaves:
                    if self.dfs(word[i+1:], curr.leaves[k]):
                        return True
                return False
        return curr.end_of_word
          
        
                
                
                
                
                
           