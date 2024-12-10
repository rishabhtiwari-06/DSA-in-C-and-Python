#include <stdio.h>
#include <stdlib.h>
int main()
{
   int rows =2;
   int columns =2;
   int **arr = (int **)malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; i++) {
        arr[i] = (int *)malloc(columns * sizeof(int));
    }

    // Initializing the array
    arr[0][0] = 1; arr[0][1] = 2;
    arr[1][0] = 3; arr[1][1] = 4;
   for (int j = 0; j < columns; j++)
   {
      if(j != 0){
         for (int i = rows-1; i >=0; i--)
         {
            printf("%d",arr[i][j]);           
         }                                     
         printf("\n"); 
      }
      else{
         for (int i = 0; i < rows; i++)
         {
            printf("%d",arr[i][j]);
         }
         printf("\n");
      }
   }
   
 
   return 0;
}
 