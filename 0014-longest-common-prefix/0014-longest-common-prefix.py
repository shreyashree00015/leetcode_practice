class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        if not arr:
            return ''
        s = ''
        for i in range(len(arr[0])):
            c = arr[0][i]
            for j in arr:
                if i>=len(j) or j[i] != c :
                    return s
            s += c
        return s
