function binarySearch(arr: number[], target: number): [number | null, number] {
    let low = 0
    let high = arr.length - 1;
    let counter = 0;

    while (low <= high) {
        counter++
        let mid = Math.floor((low + high) / 2);
        let guess = arr[mid];

        if (guess == target) {
            return [mid, counter]
        } else if (guess > target) {
            high = mid - 1;
        } else { // guess < target
            low = mid + 1;
        }
    }

    // Return null if not found, along with the counter
    return [null, counter]
}

const target = 20;
const myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

const [result, counter] = binarySearch(myList, target);

console.log("target: ", target, "counter: ", counter, "result: ", result);