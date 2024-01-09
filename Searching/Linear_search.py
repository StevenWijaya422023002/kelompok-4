import timeit

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1  
        else:
            high = mid - 1  
    return -1  

my_sorted_list = [9, 6, 8, 7, 10, 15, 13, 22, 20 ]  
target_value = 13

start_time = timeit.default_timer()

result = binary_search(my_sorted_list, target_value)

end_time = timeit.default_timer()

runtime = end_time - start_time

print("Result:", result)
print("Runtime: {:.6f} seconds".format(runtime))