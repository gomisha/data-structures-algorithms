import time
import random

# -------------- BINARY SEARCH IMPLEMENTATION --------------
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


# -------------- BINARY SEARCH LOCAL TEST --------------
target = 20
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result, counter = binary_search(my_list, target)

print("target: ", target, "counter: ", counter, "result: ", result)

# -------------- BENCHMARK SETUP --------------
ARRAY_SIZE = 10_000_000
NUM_SEARCHES = 1_000_000

print("Array size: ", ARRAY_SIZE)
print("Number of searchs: ", NUM_SEARCHES)
print("Generating sorted array...")

array = list(range(0, ARRAY_SIZE))

print("Generating search targets...")

# half the targets will be found in the list
search_keys_found = random.choices(array, k=NUM_SEARCHES // 2)

# half the targets won't be found in the list
search_keys_not_found = []
for _ in range(NUM_SEARCHES // 2):
    value = random.randint(ARRAY_SIZE + 1, ARRAY_SIZE * 2)  # this target is outside the list
    search_keys_not_found.append(value)

# combine both sets of targets (found and not found)
search_keys = search_keys_found + search_keys_not_found

# shuffle to mix found and not found targets
random.shuffle(search_keys)

# -------------- BENCHMARK EXECUTION --------------
def benchmark_search():
    start = time.perf_counter()
    for key in search_keys:
        result, counter = binary_search(array,  key)
    end = time.perf_counter()
    return (end - start)

# -------------- RUN BENCHMARK --------------


print("running benchmark...")
elapsed = benchmark_search()
print(f"elapsed time for {NUM_SEARCHES} searches: {elapsed:0.2f} seconds")
print(f"Average per search: {elapsed / NUM_SEARCHES * 1000:.6f} ms")