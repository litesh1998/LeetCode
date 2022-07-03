class Solution:
    
    
    def getRow(self, rowIndex: int) -> List[int]:
        l=[]
        self.d={}
        for i in range(rowIndex+1):
            l.append(self.f(rowIndex,i+1))
        return l
    
    def f(self, i, j):
        if (i, j) in self.d:
            return self.d[(i, j)]
        if j==1:
            return 1
        if i==0:
            return 0
        self.d[(i, j)]=self.f(i-1, j-1)+ self.f(i-1, j)
        return self.d[(i, j)]
        