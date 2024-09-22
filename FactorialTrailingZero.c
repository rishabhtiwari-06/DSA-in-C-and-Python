
#include <stdio.h>

int trailingZeroes(int n) {
    int count = 0;
    while (n >= 5) {
        n /= 5;
        count += n;  
    }
    return count;
}

int main() {
    int n = 25;
    int result = trailingZeroes(n);
    printf("%d\n", result);  // This will print 156
    return 0;
}
