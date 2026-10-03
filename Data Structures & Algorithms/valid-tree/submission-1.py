class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n-1:
            return False

        adj = [[]for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        return self.dfs(0,-1,visited,adj) and len(visited)==n

    def dfs(self,node,parent,visited,adj):
        if node in visited:
            return False
        visited.add(node)
        for it in adj[node]:
            if it == parent:
                continue
            if not self.dfs(it,node,visited,adj):
                return False
        return True