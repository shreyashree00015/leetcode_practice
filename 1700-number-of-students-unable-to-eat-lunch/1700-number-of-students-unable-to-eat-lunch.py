class Solution:
    def atEnd(self,s:List[int]) -> List[int]:
        a = s.pop(0)
        s.append(a)
        return s
    
    def countStudents(self, s: List[int], sa: List[int]) -> int:
        f = 0
        ppl = len(sa)
        
        while s:
            if s[0] == sa[0]:
                s.pop(0)
                sa.pop(0)
                ppl -= 1
                f = 0
            else:
                s = self.atEnd(s)
                f += 1
                if f == ppl:
                    return ppl
        return 0