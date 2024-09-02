#include <stdio.h>

int main(){
    char s[] =  "Hello";
    int l=0;
    for (int i =0; s[i] != '\0' ;i++)
    {
        l++;
    }
    for (int i =l-1; i>=0 ;i--)
    {
        printf("%c",s[i]);
    }
    
    return 0;
}
