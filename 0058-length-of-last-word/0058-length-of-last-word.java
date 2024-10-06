class Solution {
    public int lengthOfLastWord(String s) {
        int lastWord = 0;
        
        for(int i=s.length()-1;i>-1;i--){
            if(s.charAt(i) != ' '){
                lastWord += 1;
            }
            else if (lastWord>0 && s.charAt(i) == ' '){
                return lastWord;
            }
            
        }
        return lastWord;
    }
}