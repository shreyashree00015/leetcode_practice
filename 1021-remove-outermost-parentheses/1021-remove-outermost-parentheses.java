class Solution {
    public String removeOuterParentheses(String s) {
        String s2 = "";
        int st = 0;
        
        for(int i=0;i<s.length();i++){
            if (s.charAt(i) == '('){
                st= st + 1;
                if (st>1){
                    s2 = s2 + s.charAt(i);
                }
            }
            
            else if (s.charAt(i) == ')'){
                st= st - 1;
                if (st>0){
                    s2 = s2 + s.charAt(i);
                }
            } 
        }
        return s2;
    }
}