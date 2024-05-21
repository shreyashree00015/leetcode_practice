class Solution {
    public int subsetXORSum(int[] nums) {
        return subsetXORSumHelper(nums, 0, 0);
    }
    
    private int subsetXORSumHelper(int[] nums, int index, int currentXOR) {
        // Base case: if we have considered all elements
        if (index == nums.length) {
            return currentXOR;
        }
        
        // Calculate the sum of XORs including the current element
        int withCurrent = subsetXORSumHelper(nums, index + 1, currentXOR ^ nums[index]);
        
        // Calculate the sum of XORs excluding the current element
        int withoutCurrent = subsetXORSumHelper(nums, index + 1, currentXOR);
        
        // Return the total sum
        return withCurrent + withoutCurrent;
    }
}