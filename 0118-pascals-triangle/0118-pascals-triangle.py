class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        elif numRows==2:
            return [[1],[1,1]]
        else:
            li = [[1],[1,1]]
            end = 1
            for i in range(2,numRows):
                j = 0
                lo = [1]
                while j<end:
                    a = li[i-1][j]+li[i-1][j+1]
                    lo.append(a)
                    j+=1
                lo.append(1)
                li.append(lo)
                end+=1
            return(li)