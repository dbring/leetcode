/*
Top Down DP

To determine base cases consider the examples
(1) Both empty strings => return true;
(2) s = "", p ="****" => continue matching
(3) s = "a", p = "" => return false;

The * character presents us with a decision => match the prev char, or do not match the prev char.
*/
// T:O(m*n) S:O(m*n) where m = string.length and n = pattern.length
const doStringsMatch = (i, j, string, pattern, memo) => {
    const key = `${i},${j}`;

    if(i === string.length && j === pattern.length) return true;
    if(j === pattern.length) return false;
    if(key in memo) return memo[key];

    const charsMatch = i < string.length && (string[i] === pattern[j] || pattern[j] === '.');

    if(pattern[j + 1] === '*'){
        const continueMatching = charsMatch && doStringsMatch(i + 1, j, string, pattern, memo);
        const doneMatching = doStringsMatch(i, j + 2, string, pattern, memo);
        memo[key] = continueMatching || doneMatching;
        return memo[key]
    }

    if(charsMatch){
        memo[key] = doStringsMatch(i + 1, j + 1, string, pattern, memo);
        return memo[key]
    }

    memo[key] = false;
    return memo[key]
}

const isMatch = (string, pattern) => {
    const memo = {};
    return doStringsMatch(0, 0, string, pattern, memo)
}

/*
Bottom Up DP

First we fill in the first row of the DP array, which corresponds to the base case where s = "".
*/
// TC: O(m*n), SC: O(m*n) where m = string.length and n = pattern.length;
const createGrid = (numRows, numCols, fillValue) => {
    const grid = new Array(numRows).fill(fillValue);
    for(let i = 0; i < numRows; i++){
        grid[i] = new Array(numCols).fill(fillValue);
    }
    return grid;
}

const charsMatch = (char1, char2) => char1 === char2 || char2 === ".";

const isMatch = (s, p) => {
    const dp = createGrid(s.length + 1, p.length + 1, false);
    dp[0][0] = true;
    
    // Compute base case where s = ""
    for(let col = 2; col < dp[0].length; col += 2){
        if(p[col - 1] === "*" && dp[0][col - 2]){
            dp[0][col] = true;
        }
    }

    for(let row = 1; row < dp.length; row++){
        for(let col = 1; col < dp[0].length; col++){
            const charS = s[row - 1];
            const charP = p[col - 1];
            
            if(charsMatch(charS, charP)){
                dp[row][col] = dp[row - 1][col - 1]; // chars match
            } else if (charP === "*") {
                const prevCharP = p[col - 2];
                
                if(!charsMatch(charS, prevCharP)){
                    dp[row][col] = dp[row][col - 2]; // dont match
                } else {
                    dp[row][col] = dp[row][col - 2] || dp[row - 1][col] //dont match or match
                }
            }
        }
    }
    
    return dp[s.length][p.length]
}

/*
Bottom Up DP Space Optimized
*/
// T: O(m*n), S: O(n) where m = s.length and n = p.length;

const isMatch = (s, p) => {
    let prevRow = new Array(p.length + 1).fill(false);
    prevRow[0] = true;
    
    for(let col = 2; col < prevRow.length; col += 2){
        if(p[col - 1] === "*" && prevRow[col - 2]){
            prevRow[col] = true;
        }
    }
    for(let row = 1; row < s.length + 1; row++){
        const nextRow = new Array(p.length + 1).fill(false);
        
        for(let col = 1; col < p.length + 1; col++){
            const charS = s[row - 1];
            const charP = p[col - 1];
            
            if(charsMatch(charS, charP)){
                nextRow[col] = prevRow[col - 1]; // chars match
            } else if (charP === "*") {
                const prevCharP = p[col - 2];
                
                if(!charsMatch(charS, prevCharP)){
                    nextRow[col] = nextRow[col - 2]; // dont match
                } else {
                    nextRow[col] = nextRow[col - 2] || prevRow[col] //dont match or match
                }
            }
        }

        prevRow = nextRow;
    }
    
    return prevRow[p.length]
}