"""

140. Word Break II
Hard

2558

419

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


s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]


cat


"""


class Solution:
    def word_break2(self, s, words_dict):
        
        def backtrack(index, curr):
            if index == len(s):
                res.append(" ".join(curr))
                return 
            
            for i in range(index, len(s)):
                word = "".join(s[index:i+1])
                if word not in words_set:
                    continue
                backtrack(i+1, curr + [word])
                    
        
        
        res = []
        words_set = set(words_dict)
        backtrack(0, [])
        return res
sol = Solution()
print(sol.word_break2("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
        