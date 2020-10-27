


class Node:
    def __init__(self, val, key = None, freq= None):
        self.val = val
        self.key = key
        self.freq = freq
    


class DLList :
    def __init__(self):
        self.head = None
        self.tail = None




class LFUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.key_node_dic = {}  #<interger, node>
        self.freq_map = {}  # Map<Integer, DLList>
        self.capacity = capacity
    
    
    def updateFreq(self, node){
       DLList list = listsByFreq.get(node.freq);
	  list.remove(node);
	  node.freq++;
	  DLList listToMove = listsByFreq.get(node.freq);
	  list.addToTop(node);
    }

        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_node_dic:
            return -1
        node = self.key_node_dic[key]
        dl_list = self.freq_map[node.freq]
        dl_lsit.remove(node)
        node.freq += 1
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        




