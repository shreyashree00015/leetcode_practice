class Solution {
    public boolean isPalindrome(int x) {
        String s = x + "";
        int ptr = s.length()-1;
        for(int i = 0;i<s.length();i++){
            if (s.charAt(i) != s.charAt(ptr)){
                return false;
            }
            ptr -=1;
        }
        return true;
    }
}