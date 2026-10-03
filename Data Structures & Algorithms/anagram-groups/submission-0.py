class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        ans=[]
        sorted_list=[]
        for i in strs:
            sorted_list.append("".join(sorted(i)))
        
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                group = []
                for j in range(i, n):
                    if sorted_list[i] == sorted_list[j]:
                        group.append(strs[j])
                        visited[j] = True
                ans.append(group)
        return ans