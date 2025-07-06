package main

import "fmt"

func main() {
	// write binary search algorithm
	target := 3
	result, counter := binarySearch([]int{1, 2, 3, 4, 5}, target)

	fmt.Println("target: ", target, " counter: ", counter, " result: ", result)
}

func binarySearch(array []int, target int) (int, int) {
	left := 0
	right := len(array) - 1
	counter := 1
	for left <= right {
		mid := left + (right-left)/2
		if array[mid] == target {
			return mid, counter
		}
		if array[mid] < target {
			left = mid + 1
			counter++
			continue
		}
		if array[mid] > target {
			counter++
			right = mid - 1
		}
	}
	return -1, counter
}
