package main

import "fmt"

func main() {
	// write binary search algorithm
	target := 5
	result, counter := binarySearch([]int{1, 2, 3, 4, 5}, target)

	fmt.Println("target: ", target, " counter: ", counter, " result: ", result)
}

func binarySearch(array []int, target int) (int, int) {
	low := 0
	high := len(array) - 1
	counter := 1
	for low <= high {
		//mid := low + (high-low)/2
		mid := (low + high) / 2
		guess := array[mid]
		if guess == target {
			return mid, counter
		}
		if guess < target {
			low = mid + 1
			counter++
			//continue
		}
		if guess > target {
			counter++
			high = mid - 1
		}
	}
	return -1, counter
}
