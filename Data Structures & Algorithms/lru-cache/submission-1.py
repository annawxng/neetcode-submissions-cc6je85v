class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self.capacity = capacity
        # sentinel values
        self.head = Node(0,0)
        self.tail = Node(0,0)
        # connect them first
        self.head.next = self.tail
        self.tail.prev = self.head

    # A <-> Bn <-> C

    # B <->
    
    def _remove(self, node): # no null checks needed bc sentinels guarantee non-null neighbors
        node.prev.next = node.next
        node.next.prev = node.prev

    # head <-> A <-> B <-> C <-> D  == add A
    def _add_front(self, node):
        node.prev = self.head
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node


    # "move to front" mechanism -- _remove(if alr exists) then _add_front,

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        self._remove(self.mp[key])
        self._add_front(self.mp[key])
        return self.mp[key].val
    # if exists, update val + move to front
    # if not, create mp entry, + move to front
    # if size > capacity -> evict node at tail.prev, delete from mp
    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.mp[key].val = value
            self._remove(self.mp[key])
            self._add_front(self.mp[key])
        else:
            new_node = Node(key, value)
            self.mp[key] = new_node
            self._add_front(self.mp[key])
        if len(self.mp) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.mp[lru.key]


        
