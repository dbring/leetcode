/*
Top Down DP
*/

// T:O(n*t) S:O(n*t) where n = nums.length and t = sum(nums);
const countExpressionsThatSumToTarget = (index, sum, nums, target, memo) => {
    const key = `${index},${sum}`;
    if(index === nums.length && sum === target) return 1;
    if(index === nums.length) return 0;
    if(key in memo) return memo[key];

    memo[key] = countExpressionsThatSumToTarget(index + 1, sum + nums[index], nums, target, memo) + countExpressionsThatSumToTarget(index + 1, sum - nums[index], nums, target, memo)

    return memo[key];
}

const findTargetSumWays = (nums, target) => {
    const memo = {};
    const startingIndex = 0;
    const startingSum = 0;
    return countExpressionsThatSumToTarget(startingIndex, startingSum, nums, target, memo);
}

/*
Bottom Up DP

The first thing to note here is that the target can range from -S to +S where S is the sum of the nums array, since all numbers in nums are nonnegative.

We can map these possible targets to the range 0 to 2*S + 1.


*/

// T:O(n * t), S:O(t) where n = nums.length, t = sum(nums)
const PLACEHOLDER = 0;

const findSumOfArray = array => {
    let sumOfArray = 0;
    for(const num of array){
        sumOfArray += num;
    }
    return sumOfArray;
}

const findTargetSumWays = (nums, target) => {
    const sumOfNums = findSumOfArray(nums);
    if(Math.abs(target) > sumOfNums) return 0;

    let waysToBuildSums = new Array(2 * sumOfNums + 1).fill(PLACEHOLDER);
    waysToBuildSums[nums[0] + sumOfNums] = 1;
    waysToBuildSums[sumOfNums - nums[0]] += 1;
    
    for(let i = 1; i < nums.length; i++){
        const nextRow = new Array(2 * sumOfNums + 1).fill(PLACEHOLDER);

        for(let targetSum = 0; targetSum < 2 * sumOfNums + 1; targetSum++){
            if(waysToBuildSums[targetSum] <= 0) continue;
            
            nextRow[targetSum + nums[i]] += waysToBuildSums[targetSum];
            nextRow[targetSum - nums[i]] += waysToBuildSums[targetSum]; 
        }
        
        waysToBuildSums = nextRow;
    }
    
    return waysToBuildSums[target + sumOfNums];
}