class Solution {
    public int[] plusOne(int[] digits) {
        if(digits[digits.length-1] != 9){
            digits[digits.length-1] ++;
        }
        else{
            int i = 1;
            while(i <= digits.length && digits[digits.length-i] == 9){
                digits[digits.length-i] = 0;
                if(digits.length == 1) {
                    int[] temp = {1,0};
                    digits = temp;
                    return digits;
                }
                i++;
            }
            if(digits[0] == 0){
                int[] temp = new int[digits.length+1];
                temp[0] = 1;
                for(int t = 1; t < digits.length+1; t++){
                    temp[t] = 0;
                }
                digits = temp;
                return digits;
            }
            if(digits[digits.length-i] != 0) {
                digits[digits.length-i] ++;
            }
        }
        return digits;
    }
}