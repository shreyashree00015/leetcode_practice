class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        li = [[1],[1,1]]
        end = 1
        if rowIndex>1:
            for i in range(2,rowIndex+1):
                j = 0
                lo = [1]
                while j<end:
                    a = li[i-1][j]+li[i-1][j+1]
                    lo.append(a)
                    j+=1
                lo.append(1)
                li.append(lo)
                end+=1
        return li[rowIndex]