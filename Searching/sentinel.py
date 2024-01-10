import time

def sentinel_search(arr, target):
    start_time = time.time()

    arr.append(target)
    i = 0
    while arr[i] != target:
        i += 1

    end_time = time.time()
    elapsed_time = end_time - start_time

    if i < len(arr) - 1:
        return f"Target {target} ditemukan pada indeks {i}\nWaktu eksekusi: {elapsed_time} detik"
    else:
        return f"Target {target} tidak ditemukan dalam array\nWaktu eksekusi: {elapsed_time} detik"


array = [1, 2, 3, 4, 5]
target_value = 3

result = sentinel_search(array, target_value)
print(result)
