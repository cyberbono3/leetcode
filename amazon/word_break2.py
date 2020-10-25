"""

140. Word Break II
Hard

2560

420

Add to List

Share
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]





"""


class TrieNode:
    def __init__(self):
        self.leaves = {}
        self.end_word = False
        self.word = None
        
class Trie:
    def __init__(self):
        self.trie  = TrieNode()
        self.cache = {}
        
    def insert(self, word):
        curr = self.trie
        for ch in word:
            if ch not in curr.leaves:
                curr.leaves[ch] = TrieNode()
            curr = curr.leaves[ch]
        curr.end_word = True
        curr.word = word
        
    def cache(func):
        def inner(obj, s):
            if s not in obj.cache:
                obj.cache[s] = func(obj,s)
            return obj.cache[s]
        return inner
    
    
    @cache
    def search(self, word, current, res):
        if not word:
            res.append(" ".join(current))
            return
        
        curr = self.trie
        
        for i,ch in enumerate(word):
            if ch not in curr.leaves:
                break
            if curr.end_word:
                self.search(word[i+1:], current + [curr.word], res)      
            curr = curr.leaves[ch]
        
            
        


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        
        s = "catsanddog"
        
        
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        
        
        
        """
        trie = Trie()
        for w in wordDict:
            trie.insert(w)
        res = []
        trie.search(s, [], res)
        return res
        