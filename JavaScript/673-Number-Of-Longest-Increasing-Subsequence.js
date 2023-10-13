/* Bottom Up DP

This problem builds on problem 300, Longest Increasing Subsequence.

We initialize a counts array where counts[i] represents the number of longest increasing subsequences that end at i.

We build the LIS dp array as usual, however instead of setting LIS[i] = Math.max(LIS[i], LIS[j] + 1), we break this into two cases.

Case I: LIS[i] < LIS[j] + 1.
        In this case, we update LIS, since we have found a longer subsequence.
        We also update the counts[i] to be the number of longest increasing subsequences ending at j, that is counts[j]
        For example, say there are 5 LIS ending at j.
        We have found one more number at i at can be added to those 5 subsequences. This does not increase the count but the ith count should be the same as the jth count.

Case II: LIS[i] === LIS[j] + 1.
        This means we have found another subsequence with the same length.
        So we update increase counts[i] by counts[j]
*/
const findNumberOfLIS = (nums) => {
    const LIS = new Array(nums.length).fill(1);
    const counts = new Array(nums.length).fill(1)
    
    for(let i = 1; i < LIS.length; i++){  
        for(let j = 0; j < i; j++){
            if(nums[i] <= nums[j]) continue;
            
            if(LIS[i] < LIS[j] + 1){
                LIS[i] = LIS[j] + 1;
                counts[i] = counts[j];
            } else if (LIS[i] === LIS[j] + 1){
                counts[i] += counts[j]
            }
        }
    }

    const lengthOfLIS = Math.max(...LIS);
    let freqOfLIS = 0;
    
    for(let i = 0; i < LIS.length; i++){
        if(LIS[i] === lengthOfLIS){
            freqOfLIS += counts[i];
        }
    }
    
    return freqOfLIS;
};