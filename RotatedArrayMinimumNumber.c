#include<stdio.h>
int findMin(int* nums, int numsSize) {
    int left =0;
    int right = numsSize-1;
    while (left<right)
    {
        int mid = left + (right - left)/2;
        if (nums[mid]>nums[right])
        {
            left = mid+1;
        }
        else{
            right = mid;
        }
    }
    return nums[left];
    
}
int main(){
    int nums[]={11,13,15,17};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int c=findMin(nums,numsSize);
    printf("%d",c);
    
    return 0;
}
