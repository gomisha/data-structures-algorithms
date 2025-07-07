public class BinarySearch {
    public static int[] binarySearch(int[] arr, int target) {
        int low = 0;
        int high = arr.length - 1;
        int counter = 0;

        while (low <= high) {
            counter++;
            int mid = (low + high) / 2;
            int guess = arr[mid];

            if(guess == target) {
                return new int [] {mid, counter};
            } else if(guess > target) {
                high = mid - 1;
            } else { // guess < target
                low = mid + 1;
            }

        }
        // Return -1 if not found, along with the counter
        return new int [] {-1, counter};
    }

    public static void main(String[] args) {
        int[] arr = {0, 1,2,3,4,5,6,7,8,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
        int target = 20;
        int[] result = binarySearch(arr, target);

        System.out.println("target: " + target + " counter: " + result[1] + " result: " + result[0]);
    }
}