/*
Bottom Up DP.
0-1 knapsack problem.

First we remove duplicates because we know that if we choose any number N, we can take ALL occurances of N and it won't result in any more deletions. 

To do this we need to first keep a count of all the numbers in a map.
Then we turn the array into a set, then turn that set into an array.

We then sort the newly created unique set. This allows us to compare neighboring values and essentially turns this problem into House Robber.
*/
// TC: O(nlogn) SC: O(n)
const getCountsOfNums = nums => {
    const counts = {};
    for(const n of nums){
        counts[n] = (counts[n] || 0) + 1;
    }
    return counts;
}

const deleteAndEarn = (nums) => {
    const numCounts = getCountsOfNums(nums);
    const uniqueSet = new Set(nums);
    const uniqueNums = Array.from(uniqueSet);
    uniqueNums.sort((a, b) => a - b);

    let backTwo = 0;
    let backOne = 0;
    
    for(let i = 0; i < uniqueNums.length; i++){
        let curPoints = uniqueNums[i] * numCounts[uniqueNums[i]];
        
        if(i > 0 && uniqueNums[i] === uniqueNums[i - 1] + 1){
            let temp = backOne;
            backOne = Math.max(backTwo + curPoints, backOne);
            backTwo = temp;
        } else {
            let temp = backOne;
            backOne = backOne + curPoints;
            backTwo = temp;
        }
    }
    
    return backOne;
};

// Top Down
// T:O(nlogn) S:O(n) where n = nums.length
const getCountsOfNums = nums => {
    const counts = {};
    for(const n of nums){
        counts[n] = (counts[n] || 0) + 1;
    }
    return counts;
}

const findMaxPoints = (i, count, uniqueNums, memo) => {
    if(i === uniqueNums.length) return 0;
    if(i in memo) return memo[i];
    
    let deleteNum;
    const points = uniqueNums[i] * count[uniqueNums[i]];
    if(uniqueNums[i] + 1 !== uniqueNums[i + 1]){
        deleteNum = points + findMaxPoints(i + 1, count, uniqueNums, memo);
    } else {
        deleteNum = points + findMaxPoints(i + 2, count, uniqueNums, memo)
    }
    
    let doNotDeleteNum = findMaxPoints(i + 1, count, uniqueNums, memo);
    memo[i] = Math.max(deleteNum, doNotDeleteNum)
    
    return memo[i]
}

const deleteAndEarn = nums => {
    const count = getCountsOfNums(nums);
    const uniqueSet = new Set(nums);
    const uniqueNums = Array.from(uniqueSet);
    uniqueNums.sort((a, b) => a - b);
    const memo = {};
    
    return findMaxPoints(0, count, uniqueNums, memo);
}