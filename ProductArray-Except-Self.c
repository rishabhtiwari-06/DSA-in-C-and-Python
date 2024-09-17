#include<stdio.h>
#include<stdlib.h>

void productExceptSelf(int* nums , int* returnSize , int numsSize){
    int* prefix = (int*)malloc(numsSize * sizeof(int));
    int* suffix = (int*)malloc(numsSize * sizeof(int));

    prefix[0] = 1;
    for (int i = 1; i < numsSize; i++) {
        prefix[i] = prefix[i-1] * nums[i-1];
    }
    suffix[numsSize-1] = 1;
    for (int i = numsSize-2; i >= 0; i--) {
        suffix[i] = suffix[i+1] * nums[i+1];
    }

    for (int i = 0; i < numsSize; i++) {
        returnSize[i] = prefix[i] * suffix[i];
    }
  
}

int main(){
    int nums[] = {1,2,3,4};
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize[numsSize]; 
    productExceptSelf(nums,returnSize, numsSize);
    for (int i = 0; i <numsSize; i++)
    {
        printf("%d\n", returnSize[i]);
    }
    return 0; 
}
