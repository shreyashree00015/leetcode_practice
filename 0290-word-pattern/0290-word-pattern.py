class Solution:
    def wordPattern(self, pattern: str, s2: str) -> bool:
        c = {}
        words_set = set()
        
        s = s2.split()
        if len(pattern) != len(s):
            return False
        
        i = 0
        for j in pattern:
            if j in c:
                if c[j] != s[i]:
                    return False
            else:
                if s[i] in words_set:
                    return False
                c[j] = s[i]
                words_set.add(s[i])
            i += 1
        return True
