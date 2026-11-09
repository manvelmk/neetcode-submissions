class PrefixNode:
    
    def __init__(self):
        self.subnodes = {}
        self.terminator = False

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()
        
    def insert(self, word: str) -> None:
        curNode = self.root

        for c in word:
            if c not in curNode.subnodes:
                curNode.subnodes[c] = PrefixNode()
            curNode = curNode.subnodes[c]
        curNode.terminator = True


    def search(self, word: str) -> bool:
        curNode = self.root

        for c in word:
            if c not in curNode.subnodes:
                return False
            else:
                curNode = curNode.subnodes[c]
        return curNode.terminator

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root

        for c in prefix:
            if c not in curNode.subnodes:
                return False
            else:
                curNode = curNode.subnodes[c]
        return True
        