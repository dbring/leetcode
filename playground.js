class Circle {
    constructor(xCoordinate, yCoordinate, radius){
        this.x = xCoordinate;
        this.y = yCoordinate;
        this.r = radius;
    }
}

// Example input:
// [new Circle(0,0,1), new Circle(1,2,12), ...]

const distanceBetweenCircleCenters = (circle1, circle2) => {
    const {x1, y1} = circle1;
    const {x2, y2} = circle2;
    const distance = Math.sqrt((x1 - x2)  ** 2 + (y1 - y2) ** 2);
    return distance;
}

const getOverlappingCircles = (parentCircle, queue, listOfCircles) => {
    const {x, y, r} = parentCircle;
    const neighborCircleIndices = [];
    for(let circleIndex = 0; circleIndex < listOfCircles.length; circleIndex++){
        const {x: xNeigh, y: yNeigh, r: rNeigh} = listOfCircles[circleIndex];
        const circlesOverlap = distanceBetweenCircleCenters(parentCircle, listOfCircles[circleIndex]) <= r + rNeigh;
        if(!circlesOverlap) continue;
        queue.push(circleIndex);
    }
    return neighborCircleIndices;
}

const determineIfAllCirclesSameGroup = listOfCircles => {
    const queue = new Queue();
    const visited = new Set();
    queue.push(0);
    visited.add(0);

    while(queue.size()){
        // Remove circle
        const indexOfCircle = queue.dequeue();
        const {x, y, r} = listOfCircles[indexOfCircle];

        // Process circle

        // Add overlapping circles
        const neighborCircleIndices = getOverlappingCircles(indexOfCircle, queue, listOfCircles);
        for(const indexOfNeighbor of neighborCircleIndices){
            if(visited.has(indexOfNeighbor)) continue;
            visited.add(indexOfNeighbor);
            queue.add(indexOfNeighbor);
        }
    }
    
    return visited.size() === listOfCircles.length;
}

//// FollowUp 1: Return Number of Circle Groups:

class Circle {
    constructor(xCoordinate, yCoordinate, radius){
        this.x = xCoordinate;
        this.y = yCoordinate;
        this.r = radius;
    }
}

const distanceBetweenCircleCenters = (circle1, circle2) => {
    const {x1, y1} = circle1;
    const {x2, y2} = circle2;
    const distance = Math.sqrt((x1 - x2)  ** 2 + (y1 - y2) ** 2);
    return distance;
}

const getOverlappingCircles = (parentCircle, queue, listOfCircles) => {
    const {x, y, r} = parentCircle;
    const neighborCircleIndices = [];
    for(let circleIndex = 0; circleIndex < listOfCircles.length; circleIndex++){
        const {x: xNeigh, y: yNeigh, r: rNeigh} = listOfCircles[circleIndex];
        const circlesOverlap = distanceBetweenCircleCenters(parentCircle, listOfCircles[circleIndex]) <= r + rNeigh;
        if(!circlesOverlap) continue;
        queue.push(circleIndex);
    }
    return neighborCircleIndices;
}

const markConnectedCircles = (circleIndex, visited) => {
    const queue = new Queue();
    queue.push(circleIndex);
    visited.add(circleIndex)

    while(queue.size()){
        // Remove circle
        const indexOfCircle = queue.dequeue();
        const {x, y, r} = listOfCircles[indexOfCircle];

        // Process circle

        // Add overlapping circles
        const neighborCircleIndices = getOverlappingCircles(indexOfCircle, queue, listOfCircles);
        for(const indexOfNeighbor of neighborCircleIndices){
            if(visited.has(indexOfNeighbor)) continue;
            visited.add(indexOfNeighbor);
            queue.add(indexOfNeighbor);
        }
    }
}

const determineIfAllCirclesSameGroup = listOfCircles => {
    let numberOfCircleGroups = 0;
    const visited = new Set();
    for(let circleIndex = 0; circleIndex < listOfCircles.length; circleIndex++){
        if(visited.has(circleIndex)) continue;
        numberOfCircleGroups++;
        visitedConnectedCircles(circleIndex, visited)
    }
    return numberOfCircleGroups;
}

// FollowUp 2: return the k largest circle groups
class CircleGroup {
    constructor(circlesInGroup) {
        this.circlesInGroup = circlesInGroup;
    }
}

class CircleGroups {
    constructor(circlesInGroup){
        this.circleGroups = circleGroups; // [ new CircleGroup, new CircleGroup ...]
    }
}

class Circle {
    constructor(xCoordinate, yCoordinate, radius){
        this.x = xCoordinate;
        this.y = yCoordinate;
        this.r = radius;
    }
}

const distanceBetweenCircleCenters = (circle1, circle2) => {
    const {x1, y1} = circle1;
    const {x2, y2} = circle2;
    const distance = Math.sqrt((x1 - x2)  ** 2 + (y1 - y2) ** 2);
    return distance;
}

const getOverlappingCircles = (parentCircle, queue, listOfCircles) => {
    const {x, y, r} = parentCircle;
    const neighborCircleIndices = [];
    for(let circleIndex = 0; circleIndex < listOfCircles.length; circleIndex++){
        const {x: xNeigh, y: yNeigh, r: rNeigh} = listOfCircles[circleIndex];
        const circlesOverlap = distanceBetweenCircleCenters(parentCircle, listOfCircles[circleIndex]) <= r + rNeigh;
        if(!circlesOverlap) continue;
        queue.push(circleIndex);
    }
    return neighborCircleIndices;
}

const visitedConnectedCircles = (circleIndex, visited) => {
    const circleGroup = new CircleGroup();
    const queue = new Queue();
    queue.push(circleIndex);
    visited.add(circleIndex)
    circleGroup.circlesInGroup.push(listOfCircles[circleIndex])

    while(queue.size()){
        // Remove circle
        const indexOfCircle = queue.dequeue();
        const {x, y, r} = listOfCircles[indexOfCircle];

        // Process circle

        // Add overlapping circles
        const neighborCircleIndices = getOverlappingCircles(indexOfCircle, queue, listOfCircles);
        for(const indexOfNeighbor of neighborCircleIndices){
            if(visited.has(indexOfNeighbor)) continue;
            visited.add(indexOfNeighbor);
            queue.add(indexOfNeighbor);
            circleGroup.circlesInGroup.push(listOfCircles[indexOfNeighbor])
        }
    }

    return circleGroup;
}

const determineIfAllCirclesSameGroup = (listOfCircles, k) => {
    const minHeap = new MinHeap();
    const visited = new Set();

    for(let circleIndex = 0; circleIndex < listOfCircles.length; circleIndex++){
        if(visited.has(circleIndex)) continue;

        const circleGroup = visitedConnectedCircles(circleIndex, visited);
        minHeap.enqueue(circleGroup, circleGroup.circlesInGroup.length)

        if(minHeap.size() > k) minHeap.dequeue()
    }
    const kLargestCircleGroups = new CircleGroups(minHeap.toArray())
    return kLargestCircleGroups;
}