/*
Top Down DP.
This is an unbounded knapsack problem, similar to Coin Change.
*/
// TC: O(n^(3/2)), SC:O(n)
const FOUND_VALID_SUM = 0;
const INVALID_SUM = Infinity;

const countMinPerfectSquares = (targetNum, memo) => {
    if(targetNum === 0){
        return FOUND_VALID_SUM;
    }

    if(targetNum < 0){
        return INVALID_SUM;
    }

    if(targetNum in memo) return memo[targetNum];
    
    let count = INVALID_SUM;
    for (let i = 1; i <= targetNum; i++){
        if(i ** 2 > targetNum) break;
        count = Math.min(count, 1 + countMinPerfectSquares(targetNum - i ** 2, memo));
    }
    
    memo[targetNum] = count
    return count;
}

const numSquares = (n) => {
    const memo = {};
    return countMinPerfectSquares(n, memo);
};

// Bottom Up DP
// TC: O(n^(3/2)), S:O(n)
const PLACEHOLDER = Infinity;

const numSquares = n => {
    const minPerfectSquares = new Array(n + 1).fill(PLACEHOLDER);
    minPerfectSquares[0] = 0;
    
    for(let target = 0; target < minPerfectSquares.length; target++){
        for(let s = 1; s <= target; s++){
            const square = s ** 2;
            if(square > target) break;
            minPerfectSquares[target] = Math.min(minPerfectSquares[target], 1 + minPerfectSquares[target - square])
        }
    }
    
    return minPerfectSquares[n]
}