'''

class Solution {
    public int maxArea(int[] height) {
//         int area = 0;
//         int max = 0;

//         for(int i = 0; i < height.length; i++){
//             for(int j = i+1; j < height.length; j++){
//                 if(height[j] >= height[i]){
//                     area = height[i]*(j-i);
//                 }
//                 else{
//                     area = height[j] * (j-i);
//                 }
//                 if(max < area){
//                     max = area;
//                 }

//             }
//         }
//         return max;
        int max = 0;
        int l = 0;
        int r = height.length - 1;
        while(l < r){
            max = Math.max(max, Math.min(height[l],height[r])*(r-l));
            if(height[l] < height[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return max;

    }
}
'''