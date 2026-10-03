from collections import deque
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[]*n for _ in range(n)]
        for u,v in prerequisites:
            adj[v].append(u)

        print(adj)

        in_deg = [0]*n
        for c in adj:
            for i in range(len(c)):
                in_deg[c[i]]+=1
        q = deque()
        for i in range(n):
            if in_deg[i]==0:
                q.append(i)
        res =[]
        while q:
            node = q.popleft()
            res.append(node)
            for it in adj[node]:
                in_deg[it] -= 1
                if in_deg[it]==0:
                    q.append(it)

        print(q)
        return res if len(res)==n else []