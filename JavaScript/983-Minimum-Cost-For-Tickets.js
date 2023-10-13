/*
Bottom Up DP.

We initialize our dp array with length equal to the max element in the days array (located at the last index since the array is sorted).

We also initialize the travelDays set.

As we iterate through our DP array we have two cases: we are on a travel day or we're not - which we can find out by checking our travelDays set.

Travel Day: we look back 1, 7 and 30 days add their respective ticket costs and take the minimum. If the 7 or 30 go out of bounds, we just take their respective costs.

Non-Travel Day: 
We don't do anything to the costs, i.e. dp[i] = dp[i - 1]
*/

// T:O(max(days)), S:O(max(days) + n) where n is days.length
// In this case since at most n = max(days) = 365, we have T:O(1) and S:O(1)
const mincostTickets = (days, costs) => {
    const minCostToTravel = new Array(days.at(-1) + 1).fill(-1);
    const travelDays = new Set(days)
    minCostToTravel[0] = 0;
    
    for(let day = 1; day < minCostToTravel.length; day++){
        if(travelDays.has(day)){
            if(day < 7){
                minCostToTravel[day] = Math.min(minCostToTravel[day - 1] + costs[0], costs[1], costs[2]);
            } else if (day < 30) {
                minCostToTravel[day] = Math.min(minCostToTravel[day - 1] + costs[0], minCostToTravel[day - 7] + costs[1], costs[2]);
            } else {
            minCostToTravel[day] = Math.min(minCostToTravel[day - 1] + costs[0], minCostToTravel[day - 7] + costs[1], minCostToTravel[day - 30] + costs[2]);
            }
        } else {
            minCostToTravel[day] = minCostToTravel[day - 1]
        }
    }

    return minCostToTravel.at(-1);
};

/*
Top Down DP.

For each day in days, we can choose to buy 1 one three tickets. This is a O(3^n) decision tree. We can memoize this to bring the time and space down to n.

Here the j index moves forward from our current day i, skipping days for which our ticket duration is valid.
*/

// T:O(n), S:O(n) where n = days.length;
const durations = [1, 7, 30]

const findNextTravelDayIndex = (startIndex, endIndex, days, k) => {
    while(endIndex < days.length && days[endIndex] < days[startIndex] + durations[k]){
        endIndex++;
    }
    return endIndex;
}

const findMinTravelCost = (daysIndex, days, cost, minCostCache) => {
    if(daysIndex === days.length) return 0;

    if(minCostCache.hasOwnProperty(daysIndex)) return minCostCache[daysIndex];

    minCostCache[daysIndex] = Infinity;

    for(let i = 0; i < durations.length; i++){
        const nextTravelDayIndex = findNextTravelDayIndex(daysIndex, daysIndex, days, i)

        minCostCache[daysIndex] = Math.min(minCostCache[daysIndex], cost[i] + findMinTravelCost(nextTravelDayIndex, days, cost, minCostCache));
    }

    return minCostCache[daysIndex];
}

const mincostTickets = (days, cost) => {
    const firstTravelDayIndex = 0;
    const minCostCache = {}
    return findMinTravelCost(firstTravelDayIndex, days, cost, minCostCache)
}