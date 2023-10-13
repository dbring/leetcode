/*
Top Down DP

If characters match, we can keep the char from s or delete it from s.
If characters do not match, we must delete from s.
*/

// T:O(m*n) S:O(m*n) where m = s.length and n = t.length
const FOUND_DISTINCT_SUBSEQUENCE = 1
const NOT_A_VALID_SUBSEQUENCE = 0

const findNumDistinctSubseq = (i, j, s, t, memo) => {
    const key = `${i},${j}`;
    
    if(i === s.length & j == t.length) return FOUND_DISTINCT_SUBSEQUENCE;
    
    if(i === s.length) return NOT_A_VALID_SUBSEQUENCE;
    
    if(key in memo) return memo[key];
    
    if(s[i] === t[j]){
        memo[key] = findNumDistinctSubseq(i + 1, j + 1, s, t, memo) + findNumDistinctSubseq(i + 1, j, s, t, memo)
    } else {
         memo[key] = findNumDistinctSubseq(i + 1, j, s, t, memo)
    }
    
    return memo[key];
}

const numDistinct = (s, t) => {
    if(t.length > s.length) return NOT_A_VALID_SUBSEQUENCE;
    const memo = {};
    const sStartIndex = 0;
    const tStartIndex = 0;
    return findNumDistinctSubseq(sStartIndex, tStartIndex, s, t, memo);
}

/*
Bottom Up Space Optimized DP

Same reasoning as above.
*/

// T:O(m*n), S:O(n) where m = s.length and n = t.length
const numDistinct = (s, t) => {
    let prevRow = new Array(t.length + 1).fill(0);
    prevRow[0] = 1;
    
    for(let row = 1; row < s.length + 1; row++){
        const nextRow = new Array(t.length + 1).fill(0);
        nextRow[0] = 1;
        
        for(let col = 1; col < prevRow.length; col++){
            if(s[row - 1] !== t[col - 1]){
                nextRow[col] = prevRow[col];
            } else {
                nextRow[col] = prevRow[col] + prevRow[col - 1];
            }
        }

        prevRow = nextRow;
    }

    return prevRow[t.length]
}
