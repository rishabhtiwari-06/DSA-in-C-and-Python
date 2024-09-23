#include <stdio.h>
int maxArea(int* height, int heightSize) {
    int left =0;
    int right = heightSize-1;
    int max =0;
    while (left<right)
    {
        int w = (right-left);
        int h = (height[left] < height[right]) ? height[left] : height[right];
        int area = h*w;
        if(area > max){
            max = area;
        }
        if (height[left] < height[right])
        {
            left++;
        }
        else
        {
            right--;
        }
          
    }
    return max;
    
}
// int maxArea(int* height, int heightSize) {
//     int prea = 0;
//     int w=0;
//     int h=0;
//     int max =0;
//     for (int i = 0; i < heightSize; i++)
//     {
//         for (int j = i+1; j < heightSize; j++)
//         {
//             w= j-i;
//             h = (height[i] < height[j]) ? height[i] : height[j];
//             prea = w * h;
//             if(prea > max){
//                 max = prea;
//             }
//         }
        
//     }
//     return max;
// }
int main()
{

    int height[] = {1,8,6,2,5,4,8,3,7};
    int heightSize = sizeof(height) / sizeof(height[0]); // Correct calculation
    int area = maxArea(height, heightSize);
    printf("%d\n", area);
    return 0;
}