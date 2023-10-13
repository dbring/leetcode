/*
Bottom Up DP
Unbounded knapsack

*/
// T:O(m*n) S:O(m) where m = amount, and n = coins.length
const PLACEHOLDER = 0;

const change = (amount, coins) => {
    const numWays = new Array(amount + 1).fill(PLACEHOLDER);
    numWays[0] = 1;
    for(const coin of coins){
        for(let i = coin; i < numWays.length; i++){
            numWays[i] += numWays[i - coin];
        }
    }
    return numWays[amount];
}