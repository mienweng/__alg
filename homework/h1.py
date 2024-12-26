def power2n_a(n):
    return 2**n

def power2n_b(n):
    if n == 0: 
        return 1
    return power2n_b(n-1) + power2n_b(n-1)

def power2n_c(n):
    if n == 0: 
        return 1
    return 2 * power2n_c(n-1)

cache = {}

def power2n_d(n):
    if n in cache:
        return cache[n]
    if n == 0:
        result = 1
    else:
        result = 2 * power2n_d(n-1)
    cache[n] = result
    return result

print('power2n_a(10)=', power2n_a(10))
print('power2n_b(10)=', power2n_b(10))
print('power2n_c(40)=', power2n_c(40))
print('power2n_d(40)=', power2n_d(40))