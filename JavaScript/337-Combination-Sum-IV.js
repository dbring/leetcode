/*
Top Down DP.
This is an unbounded knapsack problem.

For every new target number there are n decisions to be made.
*/
// T:O(t*n), S:O(t) where t = target, n = nums.length
const NO_COMBINATIONS = 0;
const COMBINATION_FOUND = 1;

const findNumberOfCombinations = (newTarget, nums, combCache) => {
    if(newTarget === 0){
        return COMBINATION_FOUND;
    }
    if(newTarget < 0) return NO_COMBINATIONS;
    
    if(newTarget in combCache) return combCache[newTarget];
    
    combCache[newTarget] = NO_COMBINATIONS;
    
    for(const n of nums){
        combCache[newTarget] += findNumberOfCombinations(newTarget - n, nums, combCache);
    }
    
    return combCache[newTarget];
}

const combinationSum4 = (nums, target) => {
    const combCache = {};
    return findNumberOfCombinations(target, nums, combCache);
};

/*
Bottom Up DP

For the target number, we look back n indices and add that combination, where n is the numbers in nums.
*/
// TC: O(t*n) SC: O(t) where t = target and n = nums.length
const combinationSum4 = (nums, target) => {
    const targetCombs = new Array(target + 1).fill(0);
    targetCombs[0] = 1;
    
    for(let curTarget = 1; curTarget < targetCombs.length; curTarget++){
        for(const num of nums){
            if(num > curTarget) continue;
            
            targetCombs[curTarget] += targetCombs[curTarget - num];
        }
    }
    const numCombinationsSummingToTarget = targetCombs[target];
    return numCombinationsSummingToTarget;
}