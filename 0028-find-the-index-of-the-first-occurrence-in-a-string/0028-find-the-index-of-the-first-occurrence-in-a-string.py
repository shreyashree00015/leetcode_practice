class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i<(len(haystack)):
            print(i,haystack[i])
            if needle[0]!=haystack[i]:
                print('rej',haystack[i])
                i+=1
            
            elif needle[0]==haystack[i]:
                print(needle,haystack[i:i+len(needle)])
                if needle==haystack[i:i+len(needle)]:
                    return i
                else:
                    i+=1
        return -1