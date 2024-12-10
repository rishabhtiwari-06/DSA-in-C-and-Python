#include<stdio.h>
int maxSubArray(int* nums, int numsSize) {
    int cSum = nums[0];
    int maxSum = nums[0];
    for (int i = 1; i < numsSize; i++)
    {
        if (nums[i]>(cSum + nums[i]))
        {
            cSum = nums[i];
        }
        else{
            cSum += nums[i];
        }
        if(cSum > maxSum){
            maxSum = cSum;
        }
        
    }
    return maxSum;
    
}
int main(){
    int nums[] = {5,4,-1,7,8};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int c = maxSubArray(nums , numsSize);
    printf("%d",c);
    return 0;
}