// 2D DP
// T:O(t1 * t2), S:O(t1 * t2) where t1 = text1.length and t2 = text2.length;
const NO_COMMON_SUBSEQUENCE = 0;

const createNewGrid = (numRows, numCols, fillValue) => {
    const grid = new Array(numRows).fill(fillValue);
    
    for(let row = 0; row < grid.length; row++){
        grid[row] = new Array(numCols).fill(fillValue);
    }
    
    return grid;
}

const longestCommonSubsequence2 = (text1, text2) => {
    const subsequenceLengths = createNewGrid(text1.length + 1, text2.length + 1, NO_COMMON_SUBSEQUENCE);
    const numRows = subsequenceLengths.length;
    const numCols = subsequenceLengths[0].length;
    
    for(let row = 1; row < numRows; row++){
        for(let col = 1; col < numCols; col++){
            if(text1[row - 1] === text2[col - 1]){
                subsequenceLengths[row][col] = subsequenceLengths[row - 1][col - 1] + 1;
            } else {
                subsequenceLengths[row][col] = Math.max(subsequenceLengths[row - 1][col], subsequenceLengths[row][col - 1]);
            }
        }
    }
    return subsequenceLengths.at(-1).at(-1);
}

// Space Optimized Solution
// T: O(t1 * t2), S: O(min(t1, t2))
const NO_COMMON_SUBSEQUENCE = 0;

const findLongerString = (string1, string2) => {
    let longerString;
    let shorterString;
    if(string1.length > string2.length){
        longerString = string1;
        shorterString = string2;
    } else {
        longerString = string2;
        shorterString = string1;
    }
    return [longerString, shorterString];
}

const longestCommonSubsequence = (text1, text2) => {
    const numRows = Math.max(text1.length, text2.length);
    const numCols = Math.min(text1.length, text2.length);

    const [longerString, shorterString] = findLongerString(text1, text2);

    let prevRow = new Array(numCols + 1).fill(NO_COMMON_SUBSEQUENCE);
    
    for(let row = 1; row < numRows + 1; row++){
        const newRow = new Array(numCols + 1).fill(NO_COMMON_SUBSEQUENCE);

        for(let col = 1; col < numCols + 1; col++){
            const charactersMatch = longerString[row - 1] === shorterString[col - 1];
            if(charactersMatch){
                newRow[col] = prevRow[col - 1] + 1;
            } else {
                newRow[col] = Math.max(newRow[col - 1], prevRow[col]);
            }
        }
        
        prevRow = newRow;
    }
    
    const lengthOfLongestCommonSubsequence = prevRow.at(-1);
    return lengthOfLongestCommonSubsequence;
}