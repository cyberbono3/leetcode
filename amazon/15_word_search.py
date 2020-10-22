"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.






"""


from collections import deque, defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        
        
        
        case 1
        hit -> hot -> dot > dog  -> cog
         1       2      3     4      5
        
        
        """
    
        
        
        # edge cases
        words_set = set(wordList)
        if not words_set :
             return 0
            
        # preprocessing step -  build dic of words that differs one character
        dic = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                new_word = "".join(word[:i]) + "*" + "".join(word[i+1:])
                dic[new_word].append(word)
         # {h*t: ["hot"]}    
                
            
        
        
        
        # find intermediate words
        
        # use bfs to fidn transformation length
        
        
        q = deque()
        q.append((beginWord, 1))
        visited = set()
        
        
        # overall TC  O(n*l)
        while q:   #O(n) the number of worss in word_listy
            w, l = q.popleft()
            visited.add(w)
            if w == endWord:
                return l
            for i in range(len(w)):  # O(l) l is max word length
                new_word = "".join(w[:i]) + "*" + "".join(w[i+1:])
                for word in dic[new_word]:
                    if word in words_set and word not in visited:
                        q.append((word, l+1))
        return 0
                   