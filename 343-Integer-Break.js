/*
Top Down DP.
Recursively get the maxProduct for all integers less than n and take the max to find the maxProduct for n.
*/
// T:O(n^2), S:O(n)
const NO_VALID_INTEGER_BREAK = -1;

const getMemoKeyString = (targetInteger, currentProduct) => `${targetInteger},${currentProduct}`;

const getMaxProduct = (targetInteger, currentProduct, numberOfBreaks, memo) => {
    const memoKey = getMemoKeyString(targetInteger, currentProduct);

    if(targetInteger === 0 && numberOfBreaks >= 2){
        return currentProduct;
    }

    if(targetInteger < 0) return NO_VALID_INTEGER_BREAK;

    if(memo.hasOwnProperty(memoKey)) return memo[memoKey];

    let maxProduct = -Infinity;

    for(let i = 1; i <= targetInteger; i++){
        maxProduct = Math.max(maxProduct, 
                              getMaxProduct(targetInteger - i, currentProduct * i, numberOfBreaks + 1, memo)
                             );
    }

    return memo[memoKey] = maxProduct;
}

const integerBreak = n => {
    const memo = {};
    const startingProduct = 1;
    const initialNumberOfBreaks = 0;
    
    return getMaxProduct(n, startingProduct, initialNumberOfBreaks, memo);
};