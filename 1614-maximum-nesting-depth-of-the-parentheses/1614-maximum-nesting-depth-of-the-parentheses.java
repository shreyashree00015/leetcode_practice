class Solution {
    static int max(int a, int b){
        if (a>b){
            return a;
        }
        else{
            return b;
        }
    }
    public int maxDepth(String s) {
        int depth = 0, o_d = 0;
        for(int i=0;i<s.length();i++){
            if (s.charAt(i)=='('){
                depth += 1;
            }
            else if (s.charAt(i)==')'){
                o_d = max(o_d,depth);
                depth -= 1;
            }
        }
        return o_d;
    }
}