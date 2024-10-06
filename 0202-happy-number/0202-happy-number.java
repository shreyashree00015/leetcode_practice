class Solution {
    public boolean isHappy(int n) {
        int a = n;
        int t = 100;

        while (t > 0) {
            int b = 0;
            while (a > 0) {
                int d = a % 10;
                b += d * d;
                a /= 10;
            }

            if (b == 1) {
                return true;
            }

            a = b;
            t--;
        }
        
        return false;
    }
}
