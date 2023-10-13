/*
2D DP.

The most obvious way to do this is to maintain a 2D grid. We can optimize space by recognizing that we could just maintain the previous row of values.
However, we can use constant space by mutating the grid values.

*/

// TC: O(mn), SC: O(1) where m = grid.length and n = grid[0].length
const minPathSum = grid => {
    const numRows = grid.length;
    const numCols = grid[0].length;
    
    for(let row = 0; row < numRows; row++){
        for(let col = 0; col < numCols; col++){
            if(row === 0 && col === 0) continue;
            
            if(row === 0){
                grid[row][col] += grid[row][col - 1];
            } else if (col === 0){
                grid[row][col] += grid[row - 1][col];
            } else {
                grid[row][col] += Math.min(grid[row - 1][col], grid[row][col - 1]);
            }
        }
    }
    
    const minimumPathSum = grid.at(-1).at(-1);
    return minimumPathSum;
}