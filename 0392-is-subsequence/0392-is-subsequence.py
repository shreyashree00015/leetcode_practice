class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr_s = 0
        ptr_t = 0
        if s == "":
            return True
        while ptr_t<len(t):
            if s[ptr_s]==t[ptr_t]:
                print(s[ptr_s],t[ptr_t],ptr_s,ptr_t)
                ptr_s += 1
                ptr_t += 1
                print("s_ptr",ptr_s,"\nlen",len(s))
                if (ptr_s == (len(s))):
                    return True
            else:
                ptr_t += 1
        return False