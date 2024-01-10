import timeit

def linear(data, cari):
        for i in range(len(data)):
            if cari == data[i]:
                print("item ada :", i)
                break
        else:
            print("item tiada")

data = [9, 6, 8, 7, 10, 15, 13, 22, 20 ]
cari = 22

start_time = timeit.default_timer()

result = linear(data, cari)

end_time = timeit.default_timer()

runtime = end_time - start_time

print("Runtime: {:.6f} seconds".format(runtime))
