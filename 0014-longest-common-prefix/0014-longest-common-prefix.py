class Solution:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        if not arr:
            return ''
        
        # prefix = ''
#         first_str = arr[0]
        
#         for i in range(len(first_str)):
#             current_char = first_str[i]
#             for other_str in arr:
#                 if i >= len(other_str) or other_str[i] != current_char:
#                     return prefix
#             prefix += current_char
        
#         return prefix
        
        s = ''
        for i in range(len(arr[0])):
            c = arr[0][i]
            for j in arr:
                if i>=len(j) or j[i] != c :
                    return s
            s += c
        return s
                    
                    
                
                
                
        
#         s = ''
#         n = len(arr)
#         p=0
#         arr = sorted(arr, key=len)
#         target = arr[0]
#         left = 0
        
#         #window
#         while (p+1)<=(n-1):
#             for i in range(left+1, len(target)):
#                 if target[left:i] in arr[p+1]:
#                     s = target[left:i]
#                     print('s',s,'p',p)
#                     p+=1
#                 else:
#                     left+=1
                    
#                 if (p+1)>(n-1):
#                     break
#         return s