class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # Return x for 0 and 1
        
        left, right = 2, x // 2  # Set search bounds

        while left <= right:
            mid = (left + right) // 2  # Find the middle point
            mid_squared = mid * mid
            
            if mid_squared == x:
                return mid  # Found the exact square root
            elif mid_squared < x:
                left = mid + 1  # Look in the right half
            else:
                right = mid - 1  # Look in the left half
        
        return right
        