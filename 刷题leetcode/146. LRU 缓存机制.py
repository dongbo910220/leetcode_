'''
https://www.bilibili.com/video/BV1Fb411V7Fg?p=2
'''
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            # print("key", node.key)
            # print("val", node.val )
            return node.val
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dic:
            node1 = self.dic[key]
            self._remove(node1)
        node = Node(key, value)
        self._add(node)
        self.dic[key] = node
        if len(self.dic) > self.cap:
            del_node = self.head.next
            # print(self.dic)
            del self.dic[del_node.key]
            self._remove(del_node)


    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node