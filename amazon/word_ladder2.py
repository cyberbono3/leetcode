

from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        
        
        layer = {}
        
        
        preprocessing step  to fidn a dict with words that differ in one character
        
        dic = defaultdict(list)
        for w in words:
            for i in range(len(w)):
                inter_word = "".join(w[:i])  + "*"  + "".join(w[i+1:])
                dic[inter_word].append(w)
        
        layer = {}
        layer[beginWord] = [[beginWord]]
        
        
        
        
        # [
         ["hit","hot","dot","dog","cog"],
         ["hit","hot","lot","log","cog"]
        ]
        
        
        hit : [hit]
        
        newLayer[hot]  = [hit, hot]
        layer[hot]  [hit,hot]
             new_layer[dot]  = [["hit,hot, "dot]]
             new_layer[lot] =  [[hit, hot, lot  ]]
             
             new_layer["dog"] = [[ hit,hot, dot, dog ]]
             new_layer["log"] = [[ hit,hot, dot, log ]]
             
             new_layer [cog ] = [ [ [hit,hot, dot, dog,cog]   ] + [ [hit,hot, lot, log, cog]  ] = 
             [ [[hit,hot, dot, dog,cog], [hit,hot, lot, log, cog]  ]
        
        n - is lentgth of wordList
        l - max length of word
        TC O(n*l)
        while layer:
            new_layer = defauldict(list)
            for w in layer.keys():
                if w == endWord:
                    return layer[w]
                for i in range(len(w)):
                    inter_word = "".join(w[:i])  + "*"  + "".join(w[i+1:])
                    for new_word in dic[inter_word]:
                        if new_word in words_set:
                            new_layer[new_word]  += [l + [new_word] for l in layer[w]]
                         
            used_keys = set(new_layer.keys())
            words_set -= used_keys
            layer = new_layer
        return 
            
            
            
            
        
        n - is lentgth of wordList
        l - max length of word
        TC O(n*l)
        """
        words_set = set(wordList)
         
        dic = defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                inter_word = "".join(w[:i])  + "*"  + "".join(w[i+1:])
                dic[inter_word].append(w)
        
        layer = {}
        layer[beginWord] = [[beginWord]]
        
        while layer:
            new_layer = defaultdict(list)
            for w in layer.keys():
                if w == endWord:
                    return layer[w]
                for i in range(len(w)):
                    inter_word = "".join(w[:i])  + "*"  + "".join(w[i+1:])
                    for new_word in dic[inter_word]:
                        if new_word in words_set:
                            new_layer[new_word]  += [l + [new_word] for l in layer[w]]       
            
            used_keys = set(new_layer.keys())
            words_set -= used_keys
            layer = new_layer
        
        return []
            
