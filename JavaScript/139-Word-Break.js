/*
Notes: We can think of Word Break as an unbounded knapsack problem.
We are trying to build the string s from the words given in wordDict.

If the substring ENDING at the partition index (s.slice(0, partition)) is true, this means that the left substring can be made up of words in the wordDict.

So we need to see if the right substring STARTING at the partition to the end index (s.slice(partition, end)) is in the wordDict. 

If so, we can set dp[end] = true. And this means that the substring s.slice(0, end) can be made up of words from the wordDict.
*/
// Bottom Up
// TC: O(n^3), SC: O(n + w) where n = s.length and w = wordDict.length;

const wordBreak = (string, wordDict) => {
    const wordDictSet = new Set(wordDict);
    const canWordBreak = new Array(string.length + 1).fill(false);
    canWordBreak[0] = true; // an empty string can always be word broken
    
    for(let end = 1; end < canWordBreak.length; end++){
        for(let partition = 0; partition < end; partition++){
            const isLeftSubstringWordBroken = canWordBreak[partition];
            if(!isLeftSubstringWordBroken) continue;
            
            const isRightSubstringInWordDict = wordDictSet.has(string.slice(partition, end));
            if(!isRightSubstringInWordDict) continue;
            
            canWordBreak[end] = true;
            break;
        }
    }
    return canWordBreak[string.length];
}

// Top Down
// T:O(n^3) S:O(n)
const wordBreak = (s, wordDict) => {
    const memo = {};
    const wordSet = new Set(wordDict);
    
    const canWordBeBroken = (index) => {
        if(index === s.length) return true;
        if(index in memo) return memo[index];
        
        for(let i = index; i < s.length; i++){
            const word = s.slice(index, i + 1);
            if(wordSet.has(word) && canWordBeBroken(i + 1)) {
                memo[index] = true;
                return true;
            }
        }
        
        memo[index] = false;
        return false
    }
    
    return canWordBeBroken(0)
}