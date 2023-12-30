
import timeit

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    m = max(len(str(x)), len(str(y))) // 2
    a, b = divmod(x, 10**m)
    c, d = divmod(y, 10**m)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    result = ac * 10**(2*m) + ad_bc * 10**m + bd
    return result


start_time = timeit.default_timer()


result = karatsuba(3876, 4567)


end_time = timeit.default_timer()


runtime = end_time - start_time


print("Result:", result)
print("Runtime: {:.6f} seconds".format(runtime))