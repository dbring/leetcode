/*
Each position i in the LIS array denotes the maximum length of the increasing subsequence that includes nums[i] as it's final number.

In order to find LIS[i] we must look at the max length of every subsequence that came previously. If nums[i] > nums[j] then we have a potential subsequence at LIS[j] to which we can add one more number, namely nums[i].
*/

// TC: O(n^2), SC: O(n) where n = nums.length;

const lengthOfLIS = nums => {
    const LIS = new Array(nums.length).fill(1);
    
    for(let i = 1; i < nums.length; i++){
        for(let j = 0; j < i; j++){
            if(nums[i] <= nums[j]) continue;
            LIS[i] = Math.max(LIS[i], LIS[j] + 1);
        }
    }
    
    const longestIncreasingSubsequence = Math.max(...LIS);
    return longestIncreasingSubsequence;
}

// Top Down DP
// T:O(n^2) S:O(n) where n = nums.length;
const LISStartingAt = (i, nums, memo) => {
    if(i === nums.length) return 0;
    
    if(i in memo) return memo[i];
    
    memo[i] = 0;
    
    for(let j = i + 1; j < nums.length; j++){
        if(nums[i] >= nums[j]) continue;
        
        memo[i] = Math.max(1 + LISStartingAt(j, nums, memo), memo[i])
    }
    
    return memo[i]
}

const lengthOfLIS = nums => {
    const memo = {};
    let lenOfLIS = 0;

    for(let i = 0; i < nums.length; i++){
        lenOfLIS = Math.max(lenOfLIS, 1 + LISStartingAt(i, nums, memo))
    }

    return lenOfLIS;
}

