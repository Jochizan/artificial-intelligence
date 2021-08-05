def numbersSum(num):
    suma = 0
    print("La suma de ", end='')
    for n in range(1, num + 1):
        suma = suma + n;
        if n != num:
            print(n, '+ ', end='')
        else:
            print(n, end='')

    print(" es: ", suma)


def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


def dividers(n):
    ans = [1]
    i = 2

    while i <= n / 2:
        if n % i == 0:
            ans.append(i)
        i += 1

    ans.append(n)
    return ans
