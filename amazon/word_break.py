"""

139. Word Break
Medium

5342

257

Add to List

Share
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false







"""

class TrieNode:
    def __init__(self):
        self.leaves = {}
        self.end_word = False
        
class Trie:
    def __init__(self):
        self.trie = TrieNode()
        self.cache = {}
        
    def insert(self, word):
        curr = self.trie
        for ch in word:
            if ch not in curr.leaves:
                curr.leaves[ch]  = TrieNode()
            curr = curr.leaves[ch]
        curr.end_word = True
            
    def cache(func):
        def method(obj, s):
            if s not in obj.cache:
                obj.cache[s] = func(obj, s)
            return obj.cache[s]
        return method
        
        

    @cache
    def search(self, word):
        if not word:
            return True
        
        curr = self.trie

        for i,ch in enumerate(word):
            if ch not in curr.leaves:
                return False
            curr = curr.leaves[ch]
            if curr.end_word:
                if self.search(word[i+1:]):
                    return True  
        return False
                








class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        
        
                                       
        l                    c
        e                    o
        e                    d
        t                    e
          endword= truwe      endWord.true
        
        
        
        """
        t = Trie()
        
        for w in wordDict:
            t.insert(w)
        
        return t.search(s)
       