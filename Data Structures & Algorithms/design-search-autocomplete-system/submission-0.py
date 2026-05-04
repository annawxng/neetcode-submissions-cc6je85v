
class TrieNode():
    def __init__(self):
        self.children = {}
        self.counts = {} # {sentence: freq}

class AutocompleteSystem:

    # root, curr_node = root, curr_sentence
    # loop through sentences and times, and we want to call insert(sentence, freq) for both, freq is the value we get from times
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.curr_sentence = ""
        self.curr_node = self.root
        for sentence, freq in zip(sentences, times):
            self.insert(sentence, freq)

    # standard trie insert, except we dont care abt is_end
    # we want to update the node.counts for each node
    def insert(self, sentence: str, frequency: int):
        node = self.root
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.counts[sentence] = node.counts.get(sentence, 0) + frequency

    # two cases
    # case 1: c is #
        # store the curr sentence ==> call insert(curr_sentence, 1)
        # reset curr_node to root, curr_sentence to "", return []
    # case 2: c is regular char
        # append c to curr_sent
        # if curr_node is not None and c is in curr_node.children
            # descend into curr_node children
        # else, its dead, we set curr_node = None and we have to return []
        # make a list of items by looping through the sent, freq in curr_node.counts
        # sort alphabetically
        # sort by descending order (negate the lambda or do reverse = True)
        # return top 3 items (u can use the [:3] if needed)
    def input(self, c: str) -> List[str]:
        if c == '#':
            self.insert(self.curr_sentence, 1)
            self.curr_node = self.root
            self.curr_sentence = ""
            return []
        else:
            self.curr_sentence += c
            if self.curr_node is not None and c in self.curr_node.children:
                self.curr_node = self.curr_node.children[c]
            else:
                # dead
                self.curr_node = None
                return []
            items = []
            for sent, freq in self.curr_node.counts.items():
                items.append((sent, freq))
            items.sort(key = lambda x: x[0])
            items.sort(key = lambda x: x[1], reverse=True)
            top3 = items[:3]
            return [sentence for sentence, freq in top3]

        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)