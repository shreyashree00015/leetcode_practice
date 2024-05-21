from typing import List
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor_of_subset(subset):
            xor_sum = 0
            for num in subset:
                xor_sum ^= num
            return xor_sum

        def find_subsets(nums):
            subsets = [[]]
            for num in nums:
                subsets += [current + [num] for current in subsets]
            return subsets

        subsets = find_subsets(nums)
        total_xor_sum = sum(xor_of_subset(subset) for subset in subsets)
        return total_xor_sum
    
#         xor_list = [0]
#         n = len(nums)
#         for i in range(n-1):
#             e = i+1
            
#             while e<n:
#                 a = nums[i]
#                 # a ^= nums[e]
#                 for j in range(i+1,e+1):
#                     a^=nums[j]
                    
#                 xor_list.append(a)
#                 e+=1
                
#         for i in range(n-2):
#             e = i+2
#             a = nums[i]
#             while e<n:
#                 a^=nums[e]
#                 xor_list.append(a)
#                 e+=1
        
#         for num in nums:
#             xor_list.append(num)
            
#         print(xor_list)
#         return sum(xor_list)
        
        