test_case = int(input())

for i in range(test_case):
    A, B = input().split()
    A = int(A)
    B = int(B)
    print(f"Case #{i+1}: {A} + {B} = {A+B}")