def alg1(n: int):
    for i in range(1, n + 1):
        for j in range(1, 2**n + 1):
            print(j, end = " ")
        print()

def alg2(n: int):
    for i in range(1, n + 1):
        for j in range(1, 2**i + 1):
            print(j, end = " ")
        print()

print("========Alg1=============")
alg1(6)
print("========Alg2=============")
alg2(6)