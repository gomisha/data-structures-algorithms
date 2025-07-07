package main

import "fmt"

func main() {
	target := 20
	result, counter := binarySearch([]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, target)

	fmt.Println("target: ", target, " counter: ", counter, " result: ", result)
}

func binarySearch(array []int, target int) (int, int) {
	low := 0
	high := len(array) - 1
	counter := 0
	for low <= high {
		counter++
		mid := (low + high) / 2
		guess := array[mid]
		if guess == target {
			return mid, counter
		} else if guess > target {
			high = mid - 1
		} else if guess < target {
			low = mid + 1
		}
	}
	return -1, counter
}
