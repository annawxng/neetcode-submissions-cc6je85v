class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
    # start at root
    # loop throuhg each char and check if its in children
    # if not, create
    # walk into child
    # set node is_end = True at end
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True 
        
    # start root
    # loop through each char
    # return False if not in children
    # at the end return if it's at the end == True
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char] # remember to move into children
        return node.is_end

    # same as search but u dont care abt is_end
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)