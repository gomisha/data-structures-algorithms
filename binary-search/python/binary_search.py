def binary_search(arr, target):
    low = 0
    high = len(arr) -1
    counter = 0

    while low <= high:
        counter += 1
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid, counter
        elif guess > target:
            high = mid - 1
        else: # guess < target
            low = mid + 1
    # Return None if not found, along with the counter
    return None, counter


target = 20
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result, counter = binary_search(my_list, target)

print("target: ", target, "counter: ", counter, "result: ", result)