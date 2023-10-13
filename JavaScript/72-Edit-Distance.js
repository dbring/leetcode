/*
Top Down DP

Explanation of the base cases:
If both strings are empty or both strings are the same, return 0
If w2 is empty, return w1.length (that's the number of edits we have to make)
If w1 is empty, return w2.length

*/

// T:O(mn) S:O(mn)
const minDistanceBetweenWords = (i, j, w1, w2, memo) => {
    const key = `${i},${j}`;
    if(i === w1.length && j === w2.length) return 0;
    if(j === w2.length) return w1.length - i;
    if(i === w1.length) return w2.length - j;
    if(key in memo) return memo[key]
    
    if(w1[i] === w2[j]){
        memo[key] = minDistanceBetweenWords(i + 1, j + 1, w1, w2, memo)
    } else {
        const del = minDistanceBetweenWords(i + 1, j, w1, w2, memo);
        const replace = minDistanceBetweenWords(i + 1, j + 1, w1, w2, memo)
        const insert = minDistanceBetweenWords(i, j + 1, w1, w2, memo)

        memo[key] = 1 + Math.min(del, replace, insert)
    }
    
    return memo[key];
}

const minDistance = (word1, word2) => {
    const memo = {};
    const word1StartIndex = 0;
    const word2StartIndex = 0;
    return minDistanceBetweenWords(word1StartIndex, word2StartIndex, word1, word2, memo);
}

/*
Bottom Up DP
Space Optimized
*/
// T:O(m*n) S:O(min(m, n));
const minDistance = (word1, word2) => {
    if(word2.length > word1.length){
        [word1, word2] = [word2, word1];
    }
    
    let prevRow = new Array(word2.length + 1).fill(0)
    
    for(let col = 1; col < prevRow.length; col++){
        prevRow[col] = 1 + prevRow[col - 1];
    }
    
    for(let row = 1; row < word1.length + 1; row++){
        const nextRow = new Array(word2.length + 1).fill(0);
        
        for(let col = 0; col < prevRow.length; col++){
            if(col === 0){
                nextRow[col] = 1 + prevRow[col];
            } else {
                if(word1[row - 1] === word2[col - 1]){
                    nextRow[col] = prevRow[col - 1];
                } else {
                    nextRow[col] = 1 + Math.min(nextRow[col - 1], prevRow[col], prevRow[col - 1]);
                }
            }
        }
        
        prevRow = nextRow;
    }
    
    return prevRow[word2.length];
}