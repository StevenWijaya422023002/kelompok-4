import timeit

def fibonacci_search(arr, target):
    start_time = timeit.default_timer()

    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_current = fib_m_minus_1 + fib_m_minus_2
    
    while fib_current < len(arr):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_current
        fib_current = fib_m_minus_1 + fib_m_minus_2
    
    offset = -1
    
    while fib_current > 1:
        i = min(offset + fib_m_minus_2, len(arr) - 1)
        
        if arr[i] < target:
            fib_current = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_current - fib_m_minus_1
            offset = i
        
        elif arr[i] > target:
            fib_current = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_current - fib_m_minus_1
        
        else:
            elapsed_time = (timeit.default_timer() - start_time) * 1000  # Konversi ke milidetik
            return f"Target {target} ditemukan pada indeks {i}\nWaktu eksekusi: {elapsed_time} milidetik"
    
    if fib_m_minus_1 and arr[offset+1] == target:
        elapsed_time = (timeit.default_timer() - start_time) * 1000  # Konversi ke milidetik
        return f"Target {target} ditemukan pada indeks {offset+1}\nWaktu eksekusi: {elapsed_time} milidetik"
    
    elapsed_time = (timeit.default_timer() - start_time) * 1000  # Konversi ke milidetik
    return f"Target {target} tidak ditemukan dalam array\nWaktu eksekusi: {elapsed_time} milidetik"


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5
result = fibonacci_search(array, target_value)
print(result)
