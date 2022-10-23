/*
This is a 0-1 Knapsack problem because we can only use each number in nums once when trying to find our target sum.

We keep track of all the partial sums that we've seen so far. 

For each number in nums, we iterate through the partialSums and add the number to each partial sum, and then add that newly computed partial sum to the set.
*/

// T:O(n*t) S:O(n*t) where n = nums.length and t = target
const sumAllNumsInArray = (array) => {
    let sum = 0;
    for(let num of array){
        sum += num;
    }
    return sum;
}

const doesPartitionExist = (i, sum, target, nums, memo) => {
    const key = `${i},${sum}`;

    if(sum > target) return false;
    if(sum === target) return true;
    if(i === nums.length) return false;
    if(key in memo) return memo[key];

    memo[key] = doesPartitionExist(i + 1, sum + nums[i], target, nums, memo) || doesPartitionExist(i + 1, sum, target, nums, memo);

    return memo[key]
}

const canPartition = nums => {
    const total = sumAllNumsInArray(nums);
    
    if(total % 2 !== 0) return false;
    
    const target = total / 2;
    
    const memo = {};
    return doesPartitionExist(0, 0, target, nums, memo)
}

// Bottom Up Space Optimized
// TC: O(n * t), S:O(t) where n = nums.length and m = targetNum
const sumAllNumsInArray = (array) => {
    let sum = 0;
    for(let num of array){
        sum += num;
    }
    return sum;
}

const canPartition = nums => {
    const sumOfNums = sumAllNumsInArray(nums);
    
    const isSumOfNumsOdd = sumOfNums % 2 !== 0;
    if(isSumOfNumsOdd) return false;
    
    const targetNum = sumOfNums / 2;
    const partialSums = new Set()
    partialSums.add(0);
    
    for(const num of nums){
        const partialSumsArray = Array.from(partialSums); // needed since we are adding new partial sums to the set
        for(const partialSum of partialSumsArray){
            partialSums.add(num + partialSum);

            if(partialSums.has(targetNum)) return true;
        }
    }
    
    return false;
}