hours, minutes = input().split()
cook_time = input()
hours, minutes, cook_time = int(hours), int(minutes), int(cook_time)

total_minutes = (hours * 60) + minutes + cook_time
hours = int(total_minutes / 60)
minutes = total_minutes % 60

if hours>=24:
    print(f"{hours-24} {minutes}")
else:
    print(f"{hours} {minutes}")


# 정수형 변수를 저장한 변수의 type은 int이다.