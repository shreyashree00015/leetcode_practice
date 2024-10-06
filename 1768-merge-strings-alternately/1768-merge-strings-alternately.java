class Solution {
    public String mergeAlternately(String word1, String word2) {
        int s1 = word1.length(), s2 = word2.length();
        int s = Math.min(s1,s2);
        String newS = "";
        int i=0;
        for(i = 0; i < s; i++){
            newS = newS + word1.charAt(i) + word2.charAt(i);
        }      
        if (s1>s2){
            for (int ni=i;ni<s1;ni++){
                newS =  newS + word1.charAt(ni);
            }
        }
        else if (s2>s1){
            for (int ni=i;ni<s2;ni++){
                newS =  newS + word2.charAt(ni);
            }
        }
        return newS;
    }
}