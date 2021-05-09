def is_prime(num):
    result = list()
    i = 1
    while num != len(result):
        i = i + 1
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            result.append(i)
    return result

def calculate_prime_number(length):

    result = is_prime(length)
    for index, prime in enumerate(result):
        print(prime, end=" ")

n = int(input("길이 : "))
print(calculate_prime_number(n))