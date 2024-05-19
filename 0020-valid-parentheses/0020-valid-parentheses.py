class Solution:
    def isValid(self, s: str) -> bool:
        
        left = 0
        right = len(s)-1
        if s[left] in ')]}' or s[right] in '({[':
            return False
        L =[]
        for i in range(len(s)):
            if s[i] in '({[':
                L.append(s[i])

            else:
                if len(L)==0:
                    return False
                if s[i]==')' and L[-1]=='(':
                    L.pop(-1)
                elif s[i]=='}' and L[-1]=='{':
                    L.pop(-1)
                elif s[i]==']' and L[-1]=='[':
                    L.pop(-1)
                else:
                    return False
                
        if L:
            return False
        return True
            
        