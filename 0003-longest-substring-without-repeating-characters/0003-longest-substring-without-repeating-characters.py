class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ch = {}
        # long = 0
        # st = 0
        # for i,c in enumerate(s):
        #     if c in ch and ch[c] >=st:
        #         st = ch[c] +1
        #     ch[c] = i
        #     long = max(long, i-st+1)
        # return long
        ls = 0
        for i in range(len(s)):
            ls1 = 0
            li = []
            end = i+1
            while end<=len(s):
                if s[end-1:end] not in li:
                    li.append(s[end-1:end])
                    ls1+=1
                else:
                    end = len(s)+1
                
                end+=1
            ls = max(ls,ls1)
        return ls
        