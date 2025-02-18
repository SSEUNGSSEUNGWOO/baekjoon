num = int(input())

for i in range(num):
    a = input().split()
    result = float(a[0])

    for idx, i in enumerate(a):
        if a[idx] == '@':
            result = result * 3
        elif a[idx] == '%':
            result = result + 5
        elif a[idx] == '#':
            result = result - 7

    print("%0.2f"%result)

    
# for i in () : ()에는 범위 혹은 리스트 
# enumerate는 인덱스 번호를 가져올 수 있다. 근데 두개의 변수를 써서 인데스번호 + 값을 받는다.