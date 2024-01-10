import timeit

def bubbleSortAsc(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

data = [9, 6, 8, 7, 1, 3, 2, 10, 15, 13, 22, 20]
print('Data sebelum di sort:', data)
print('\n')

setup_code = '''
from __main__ import bubbleSortAsc
data = [9, 6, 8, 7, 1, 3, 2, 10, 15, 13, 22, 20]
'''

execution_time = timeit.timeit(stmt='bubbleSortAsc(data.copy())', setup=setup_code, number=1000)
execution_time /= 10

print('Data ascending setelah di sort:')
bubbleSortAsc(data)
print(data)
print(f"Waktu eksekusi rata-rata: {execution_time:.6f} detik")

##################################################################################################

def bubbleSortDesc(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(0, i):
            if data[j] < data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

print('\n')

setup_code = '''
from __main__ import bubbleSortDesc
data = [9, 6, 8, 7, 1, 3, 2, 10, 15, 13, 22, 20]
'''

execution_time = timeit.timeit(stmt='bubbleSortDesc(data.copy())', setup=setup_code, number=1000)
execution_time /= 10  

print('Data descending setelah di sort:')
bubbleSortDesc(data)
print(data)
print(f"Waktu eksekusi rata-rata: {execution_time:.6f} detik")
    