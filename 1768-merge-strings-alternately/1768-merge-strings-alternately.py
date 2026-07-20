class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res_str = ''
        for i in range(len(word1)):
            res_str += word1[i]
            res_str += word2[i]
            if len(word2)<len(word1) and i+1==len(word2):
                res_str += word1[i+1:]
                break
        if len(word2)>len(word1) and i+1==len(word1):
            res_str += word2[i+1:]
        return(res_str)        