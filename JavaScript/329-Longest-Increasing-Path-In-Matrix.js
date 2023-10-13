/* 
Top Down DP
At each cell we explore all directions and only follow those directions that have larger cell values.
*/

const directions = [[1, 0], [0, 1], [-1, 0], [0, -1]];

const isInbounds = (row, col, matrix) => {
    const numRows = matrix.length;
    const numCols = matrix[0].length;
    
    const rowInbounds = row >= 0 && row < numRows;
    const colInbounds = col >= 0 && col < numCols;
    
    return rowInbounds && colInbounds;
}

const longestIncreasingPath = matrix => {
    const memo = {};
    
    const findLongestIncPathLen = (row, col) => {
        const key = `${row},${col}`;
        if(key in memo) return memo[key];
        
        
        let maxCount = 1;
        for(const [changeRow, changeCol] of directions){
            const newRow = row + changeRow;
            const newCol = col + changeCol;
            
            if(!isInbounds(newRow, newCol, matrix)) continue;
            if(matrix[newRow][newCol] <= matrix[row][col]) continue;
            maxCount = Math.max(maxCount, 1 + findLongestIncPathLen(newRow, newCol))
        }
        
        memo[key] = maxCount;
        return memo[key];
    }
    
    let lenOfLongestIncPath = 1;
    for(let row = 0; row < matrix.length; row++){
        for(let col = 0; col < matrix[0].length; col++){
            lenOfLongestIncPath = Math.max(lenOfLongestIncPath, findLongestIncPathLen(row, col));
        }
    }
    
    return lenOfLongestIncPath;
}