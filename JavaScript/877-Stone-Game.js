/*
Top Down DP.
This is a 0-1 knapsack problem.
At each turn there are two choices, the leftmost unused value or the rightmost unused value.

*/
// T:O(n^2), S:O(n^2)
const getIndicesString = (left, right) => `${left},${right}`;

const canAliceWin = (piles, left, right, scoreA, scoreB, aliceTurn, memo) => {
    const indices = getIndicesString(left, right);

    if(left > right){
        if(scoreA > scoreB) return true;
        else return false;
    }
    if(indices in memo) return memo[indices];
    
    if(aliceTurn){
        memo[indices] = canAliceWin(piles, left + 1, right, scoreA + piles[left], scoreB, !aliceTurn, memo) || canAliceWin(piles, left, right - 1, scoreA + piles[right], scoreB, !aliceTurn, memo)
    } else {
        memo[indices] = canAliceWin(piles, left + 1, right, scoreA, scoreB + piles[left], !aliceTurn, memo) || canAliceWin(piles, left, right - 1, scoreA, scoreB + piles[right], !aliceTurn, memo)
    }
    
    return memo[`${left},${right}`];
}

const stoneGame = (piles) => {
    const memo = {};
    const leftIndex = 0;
    const rightIndex = piles.length - 1;
    const aliceInitialScore = 0;
    const bobInitialScore = 0;
    const aliceTurn = true;
    return canAliceWin(piles, leftIndex, rightIndex, aliceInitialScore, bobInitialScore, aliceTurn, memo);
};