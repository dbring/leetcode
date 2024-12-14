class Node:
    def __init__(self):
        self.is_end = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        TC: O(n), SC: O(1) where n = len(word)
        """
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()

            cur = cur.children[c]

        cur.is_end = True

    def search(self, word: str) -> bool:
        """
        TC: O(n), SC: O(1) where n = len(word)
        """
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False

            cur = cur.children[c]

        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        TC: O(n), SC: O(1) where n = len(prefix)
        """
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False

            cur = cur.children[c]

        return True
