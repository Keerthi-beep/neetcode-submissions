class Trie:
    def __init__(self):
        self.node = {}
        self.flag = False

    def insert(self,path):
        cur = self
        for ch in path.split('/'):
            if ch not in cur.node:
                cur.node[ch] = Trie()
            cur = cur.node[ch]
        cur.flag = True

    def startsWith(self, prefix):
        cur = self
        folders = prefix.split('/')
        for i in range(len(folders)-1):
            cur = cur.node[folders[i]]
            if cur.flag:
                return True
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.insert(f)
                
        res = []
        for f in folder:
            if not trie.startsWith(f):
                res.append(f)
        return res         
        