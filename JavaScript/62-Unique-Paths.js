// 2D Dynamic Programming Solution
const PLACEHOLDER = 0;

const createNewGrid = (numRows, numCols, fillValue) => {
    const grid = new Array(numRows).fill(fillValue);
    for(let i = 0; i < grid.length; i++){
        grid[i] = new Array(numCols).fill(fillValue);
    }
    return grid;
}

const uniquePaths = (m, n) => {
    const partialUniquePaths = createNewGrid(m + 1, n + 1, PLACEHOLDER)
    partialUniquePaths[1][1] = 1;
    
    for(let row = 1; row < m + 1; row++){
        for(let col = 1; col < n + 1; col++){
            if(row === 1 && col === 1) continue;
            partialUniquePaths[row][col] = partialUniquePaths[row - 1][col] + partialUniquePaths[row][col - 1];
        }
    }
    
    return partialUniquePaths[m][n];
}

// 1D Dynamic Programming Solution
// TC: O(m*n), SC: O(min(m, n));
const uniquePaths = (m, n) => {
    const numRows = Math.max(m, n)
    const numCols = Math.min(m, n);
    let prevRow = new Array(numCols + 1).fill(1);
    prevRow[0] = 0;
    
    
    for(let row = 1; row < numRows; row++){
        let newRow = new Array(numCols + 1).fill(0);
        for(let col = 1; col < numCols + 1; col++){
            newRow[col] = newRow[col - 1] + prevRow[col]
        }
        prevRow = newRow;
    }
    
    return prevRow[numCols];
}