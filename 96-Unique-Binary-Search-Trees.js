/*
We need to recognize that for a given number of nodes n, we need to sum up the number of unique BSTs when the numbers 1 to n are the root node.

For example if i is the current root, then the number of unique BSTs is the number of unique BSTs formed by its left subtree (which has i - 1 nodes) multiplied by the number of unique BSTs formed by it's right subtree (which has n - i nodes).
*/
// Bottom Up
// TC:O(n^2), SC: O(n)

const numTrees = n => {
    const numUniqueBSTs = new Array(n + 1).fill(0);
    numUniqueBSTs[0] = 1;
    numUniqueBSTs[1] = 1;
    
    for(let numNodes = 2; numNodes < numUniqueBSTs.length; numNodes++){
        for(let curRoot = 1; curRoot <= numNodes; curRoot++){
            const numNodesLeft = curRoot - 1;
            const numNodesRight = numNodes - curRoot;
            numUniqueBSTs[numNodes] += numUniqueBSTs[numNodesLeft] * numUniqueBSTs[numNodesRight];
        }
    }

    return numUniqueBSTs[n];
}

// Top Down
// T:O(n^2) S:O(n)
const countUniqueBSTs = (numNodesInTree, memo) => {
    const key = `${numNodesInTree}`;

    if(numNodesInTree <= 1) return 1;
    if(key in memo) return memo[key];

    let treeCount = 0;

    for(let i = 1; i <= numNodesInTree; i++){
        const leftTreeCount = countUniqueBSTs(i - 1, memo);
        const rightTreeCount = countUniqueBSTs(numNodesInTree - i, memo)
        treeCount += leftTreeCount * rightTreeCount;
    }

    memo[key] = treeCount;
    return treeCount;
}

const numTrees = n => {
    const memo = {};
    return countUniqueBSTs(n, memo)
}