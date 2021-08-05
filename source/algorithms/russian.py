import numpy as np


def multiply(f_1, f_2, answer, acc=0):
    print([f_1, f_2, acc])
    answer.append([f_1, f_2, acc])
    f_1, f_2 = f_1 * 2, f_2 // 2

    if f_2 % 2 != 0:
        acc = acc + f_1

    if f_2 != 0:
        return multiply(f_1, f_2, answer, acc)

    print([f_1, f_2, acc])
    answer.append([f_1, f_2, acc])
    # return answer


def russian_algorithm(f_1, f_2):
    acc = 0
    answer = []

    if f_2 % 2 != 0:
        acc = f_1

    multiply(f_1, f_2, answer, acc)
    return np.array(answer)


print("Impresión normal por listas de 3 elementos")
ans = russian_algorithm(40, 20)

print()
print("Impresión en array de numpy: ")
print(ans)

print("La multiplicación es: ", end='')
print(ans[0:, 2].max())
