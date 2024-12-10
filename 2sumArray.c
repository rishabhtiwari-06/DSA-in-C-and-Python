#include<stdio.h>

int main(){
    int arr[] = {3,2,4};
    int target = 6;
    int l = sizeof(arr) / sizeof(arr[0]);
    int result[2];
    
    for (int i = 0; i < l; i++)
    {
        for (int j = i+1; j < l; j++)
        {
            if(arr[i]+arr[j]==target){
                result[0]=i;
                result[1]=j;
               
            }
        }
        
    }
    for (int i = 0; i < 2; i++)
    {
        printf("%d",result[i]);
    }
    return 0;
}
