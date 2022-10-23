/*
Top Down DP

 Note that we don't actually need to use i3 since i1 + i2 tell us the index of s3.
*/

// T:O(m * n), S:O(m * n) where m = s1.length and n = s2.length
const canStringsInterleave = (i1, i2, i3, s1, s2, s3, memo) => {
    const key = `${i1},${i2}`;
    
    if(i3 === s3.length) return true;
    if(key in memo) return memo[key];
    
    if(s1[i1] === s3[i3] && s2[i2] === s3[i3]){
        memo[key] = canStringsInterleave(i1 + 1, i2, i3 + 1, s1, s2, s2, memo) || canStringsInterleave(i1, i2 + 1, i3 + 1, s1, s2, s2, memo);
        return memo[key];
    } else if(s1[i1] === s3[i3]){
        memo[key] = canStringsInterleave(i1 + 1, i2, i3 + 1, s1, s2, s2, memo);
        return memo[key];
    } else if (s2[i2] === s3[i3]) {
        memo[key] = canStringsInterleave(i1, i2 + 1, i3 + 1, s1, s2, s2, memo);
        return memo[key];
    }  else {
        memo[key] = false;
        return memo[key];
    }
    
}

const isInterleave = (s1, s2, s3) => {
    if(s3.length !== s1.length + s2.length) return false;
    
    const memo = {};
    const string1StartIdx = 0;
    const string2StartIdx = 0;
    const string3StartIdx = 0;
    return canStringsInterleave(string1StartIdx, string2StartIdx, string3StartIdx, s1, s2, s3, memo)
}

/* Bottom Up DP */
// T:O(m * n), S:O(min(m, n)) where m = s1.length and n = s2.length

const isInterleave = (s1, s2, s3) => {
    if(s3.length !== s1.length + s2.length) return false;

    if(s2.length > s1.length){
        [s1, s2] = [s2, s1]
    }
    
    const dp = new Array(s2.length + 1).fill(false);
    dp[0] = true;
    
    for(let i = 0; i <= s1.length; i++){
        for(let j = 0; j <= s2.length; j++){
            if(i === 0 && j === 0) continue;
            
            if(i === 0){
                dp[j] = dp[j - 1] && (s2[j - 1] === s3[i + j - 1]);
            } else if (j === 0){
                dp[j] = dp[j] && (s1[i - 1] === s3[i + j - 1]);
            } else {
                dp[j] = dp[j - 1] && (s2[j - 1] === s3[i + j - 1]) || 
                        dp[j] && (s1[i - 1] === s3[i + j - 1]);
            }
        }
    }
    
    return dp[s2.length];
}