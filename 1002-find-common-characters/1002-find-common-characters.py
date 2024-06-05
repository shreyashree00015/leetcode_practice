class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cn = Counter(words[0])
        for word in words:
            cur = Counter(word)
            for c in cn:
                cn[c] = min(cn[c], cur[c])
        res = []
        for c in cn:
            for i in range(cn[c]):
                res.append(c)
        return res
    
