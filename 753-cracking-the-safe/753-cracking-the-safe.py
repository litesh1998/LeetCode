class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        ##total possible answer k**n
        ##total length n*k**n
        ##all possible password shares n-1 suffix
        totalSize = k**n
        answer = ["0"]*n
        visited = set({''.join(answer)}) 
        if self.dfs(n, k, totalSize, visited, answer):
            return ''.join(answer)
        return ''
        
    def dfs(self, n, k, totalSize, visited, answer):
        if len(visited) == totalSize:
            return True
        #prefix the current node
        node = ''.join(answer[len(answer)-n+1:])
        for i in range(k):      
            nei = node + str(i)
            if nei not in visited:
                answer.append(str(i))
                visited.add(nei)
                if self.dfs(n, k, totalSize, visited, answer):
                    return True
                visited.remove(nei)
                answer.pop()
        return False 