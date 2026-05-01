class TrieNode:
    def __init__(self):
        # children maps a character to another TrieNode.
        self.children = {}
        # is_word tells whether this node ends a complete word.
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # this inserts a word letter by letter into the trie.
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True

    def contains(self, word):
        # checks to see whether a word exists in the trie.
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.is_word

    def collect_words(self, prefix=""):
        # will return all words that begin with a given prefix.
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return []
            curr = curr.children[ch]

        words = []
        self._dfs_collect(curr, prefix, words)
        return words

    def _dfs_collect(self, node, prefix, words):
        # recursive helper to collect all words below a node.
        if node.is_word:
            words.append(prefix)

        for ch, child in node.children.items():
            self._dfs_collect(child, prefix + ch, words)