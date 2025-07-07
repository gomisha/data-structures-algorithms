function binarySearch(arr, target) {
    var low = 0;
    var high = arr.length - 1;
    var counter = 0;
    while (low <= high) {
        counter++;
        var mid = Math.floor((low + high) / 2);
        var guess = arr[mid];
        if (guess == target) {
            return [mid, counter];
        }
        else if (guess > target) {
            high = mid - 1;
        }
        else { // guess < target
            low = mid + 1;
        }
    }
    return [null, counter];
}
var target = 20;
var myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
var _a = binarySearch(myList, target), result = _a[0], counter = _a[1];
console.log("target: ", target, "counter: ", counter, "result: ", result);
