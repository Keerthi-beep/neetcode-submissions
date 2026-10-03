class Solution:
    def isPathCrossing(self, path: str) -> bool:
        mp = {'N': (0,1),'S':(0,-1),'E':(-1,0),'W':(1,0)}
        vis = set()
        start = (0,0)
        vis.add(start)
        for i in range(len(path)):
            x = start[0] + mp[path[i]][0]
            y =  start[1] + mp[path[i]][1]
            start = (x,y)
            if start in vis:
                return True
            vis.add(start)

        return False