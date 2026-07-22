class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res_list = []
        max_c = max(candies)
        for i in candies:
            if i+extraCandies>=max_c:
                res_list.append(True)
            else:
                res_list.append(False)
        return(res_list)
        