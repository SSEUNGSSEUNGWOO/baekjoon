test_case = int(input())

for i in range(test_case):
    A, B = input().split()
    A = int(A)
    B = int(B)
    print(f"Case #{i+1}: {A+B}")


# range(5)는 0, 1, 2, 3, 4 순서대로 i에 대입된다.