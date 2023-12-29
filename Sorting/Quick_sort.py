import timeit

def quickSortAsc(data):
    indeks = len(data)
    if indeks <= 1:
        return data
    else:
        pivot = data.pop()

    dataKiri = []
    dataKanan = []

    for i in data :
        if i < pivot:
            dataKiri.append(i)
        else:
            dataKanan.append(i)
    
    return quickSortAsc(dataKiri) + [pivot] + quickSortAsc(dataKanan)

data = [9, 6, 8, 7, 1, 3, 2, 10, 15, 13, 22, 20]
print('data sebelum sorting :', data)
print('\n')

setup_code = '''
from __main__ import quickSortAsc
data = [9, 6, 8, 7, 1, 3, 2, 10, 15, 13, 22, 20]
'''

execution_time = timeit.timeit(stmt='quickSortAsc(data.copy())', setup=setup_code, number=1000)
execution_time /= 10

print('data ascending sesudah sorting :')
hasil = quickSortAsc(data)
print(hasil)
print(f"Waktu eksekusi rata-rata: {execution_time:.6f} detik")

###############################################################################################

def quickSortDesc(data):
    indeks = len(data)
    if indeks <= 1:
        return data
    else:
        pivot = data.pop()

    dataKiri = []
    dataKanan = []

    for i in data :
        if i < pivot:
            dataKiri.append(i)
        else:
            dataKanan.append(i)
    
    return quickSortDesc(dataKanan) + [pivot] + quickSortDesc(dataKiri)

print('\n')

setup_code = '''
from __main__ import quickSortDesc
data = [9, 6, 8, 7, 1, 3, 2, 10, 15, 13, 22, 20]
'''

execution_time = timeit.timeit(stmt='quickSortDesc(data.copy())', setup=setup_code, number=1000)
execution_time /= 10

print('data ascending sesudah sorting :')
hasil = quickSortDesc(data)
print(hasil)
print(f"Waktu eksekusi rata-rata: {execution_time:.6f} detik")