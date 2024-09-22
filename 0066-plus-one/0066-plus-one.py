class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s+=str(i)
        re = int(s)+1
        d = []
        for i in str(re):
            d.append(int(i))
        return d