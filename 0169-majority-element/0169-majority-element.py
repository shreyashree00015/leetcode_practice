class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic_ele = {}
        for i in nums:
            if i in dic_ele:
                dic_ele[i]+=1
            else:
                dic_ele[i]=1
        return max(dic_ele,key=dic_ele.get)
        