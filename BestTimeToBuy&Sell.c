
#include<stdio.h>
int main() {
    int prices[] = {7,6,4,3,1};
    int pricesSize = sizeof(prices) / sizeof(prices[0]);
    
    if (pricesSize == 0) {
        printf("0");
        return 0;
    }
    
    int minPrice = prices[0];
    int maxProfit = 0;
    
    for (int i = 1; i < pricesSize; i++) {
        // Update the minimum price if a lower price is found
        if (prices[i] < minPrice) {
            minPrice = prices[i];
        }
        
        // Calculate the potential profit at current price and update max profit
        int profit = prices[i] - minPrice;
        if (profit > maxProfit) {
            maxProfit = profit;
        }
    }
    
    printf("%d", maxProfit);
    return 0;
}
