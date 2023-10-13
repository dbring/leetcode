/*
Top Down DP

The idea here is to go backwards and consider which balloon we should pop LAST.

We can then consider the left and right subarrays separately, and consider which balloons should be popped last from them.

The TC is n^3 because there are n^2 subarrays and we potentially need to do a linear scan of each subarray to find which balloon to pop last.
*/

// TC: O(n^3), SC: O(n^2)
const BOUNDARY = 1;

const findMaxCoins = (left, right, memo, nums) => {
    const key = `${left},${right}`
    if(left > right) return 0;
    if(key in memo) return memo[key]
    
    memo[key] = 0;
    
    for(let i = left; i <= right; i++){
        const coins = nums[left - 1] * nums[i] * nums[right + 1]
        const remaining = findMaxCoins(left, i - 1, memo, nums) + findMaxCoins(i + 1, right, memo, nums)
        memo[key] = Math.max(memo[key], coins + remaining);
    }
    
    return memo[key];
}

const maxCoins = nums => {
    const memo = {};
    nums.push(BOUNDARY);
    nums.unshift(BOUNDARY);
    const leftStartIndex = 1;
    const rightStartIndex = nums.length - 2;
    
    return findMaxCoins(leftStartIndex, rightStartIndex, memo, nums);
}