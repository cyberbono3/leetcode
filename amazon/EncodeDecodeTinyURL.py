
import random


"""

http://tinyurl.com/4e9iAk


"""


class Codec:
    alphabet  = strings.ascii_letters + '0123456789'
    
    def __init__(self):
        self.shortToUrl = {}
        
    

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        
        
        https://leetcode.com/problems/design-tinyurl
        http://tinyurl.com/4e9iAk
        
        """
        code  = "".join([random.choice(Codec.alphabet) for _ in range(6)]
        shortURL = "http://tinyurl.com" + code
        self.shortToUrl[shortURL] = longUrl

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.shortToUrl[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))