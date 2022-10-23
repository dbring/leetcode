/*
Dynammic programming problem.
Base cases: empty string = 1, and single char string = 1

Examples: "9999" returns 1 because (9 9 9 9) is the only partition.
This means that, at minimum, if the character we are at is non-zero, then we set current to the number one index back. The dp array looks like
E   9  9  9  9
[1, 1, 1, 1, 1]

Then we check is the previus char and current char form a string <= 26. If so, then we add the number of ways to decode from BEFORE the prev char.

Example: "234" returns 2 because (2 3 4) and (23 4). When we are at the 3 we look back at the 2 and see that 23 <= 26. So we treat 23 as a single character that can be added as a valid grouping. The dp array looks like:
E   2  3  4
[1, 1, 2, 2]
*/

// Top Down DP
// T:O(n), S:O(n)
const numDecodings = s => {
    if(s[0] === "0") return 0;
    
    const memo = {};
    
    const numWays = i => {
        if(i === s.length) return 1;
        if(s[i] === "0") return 0;
        if(i in memo) return memo[i];
        
        memo[i] = numWays(i + 1);
        
        if(i + 1 < s.length && (s[i] === "1" || (s[i] === "2" && s[i + 1] <= 6))) {
            memo[i] += numWays(i + 2);
        }
        
        return memo[i]
    }
    return numWays(0)
}

// Bottom Up DP
// T:O(n), S:O(n)
const numDecodings = s => {
    if(s[0] === "0") return 0;
    
    const dp = new Array(s.length + 1).fill(0);
    dp[0] = 1;
    dp[1] = 1;
    
    for(let i = 2; i < dp.length; i++){
        if(s[i - 1] !== "0"){
            dp[i] = dp[i - 1];
        } 
        
        if(s[i - 2] === "1" || (s[i - 2] === "2" && s[i - 1] <= 6)){
            dp[i] += dp[i - 2];
        }
    }
    
    return dp[s.length];
}

// Bottom Up DP Optmized Space
// T:O(n), S:O(1)
const numDecodings = string => {
    const stringStartsWithLeadingZero = string[0] === '0'
    if(stringStartsWithLeadingZero) return 0;
    
    let backTwo = 1;
    let backOne = 1;
    let current;
    
    for(let i = 1; i < string.length; i++) {
        current = 0;
        if(string[i] !== '0'){
            current = backOne;
        }
        
        const areDigitsBetween10And26 = (string[i - 1] === '1') || (string[i - 1] === '2' && string[i] <= 6);
        
        if(areDigitsBetween10And26){
            current += backTwo;
        }
        
        backTwo = backOne;
        backOne = current;
    }
    
    return backOne;
}