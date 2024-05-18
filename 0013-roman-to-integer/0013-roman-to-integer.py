class Solution:
    def romanToInt(self, s: str) -> int:
        sym_val = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        tot = 0
        val = 0
        i=0
        while i<len(s):
            if (i+1)<len(s) and sym_val[s[i+1]]>sym_val[s[i]]:
                val = sym_val[s[i+1]] - sym_val[s[i]]
                
                i+=2
            else:
                val = sym_val[s[i]]
                i+=1
            tot +=val
        return tot
        
        