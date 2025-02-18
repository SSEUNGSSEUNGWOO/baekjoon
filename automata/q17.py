hours, minutes, seconds = map(int, input().split())
cook_time = input()
cook_time = int(cook_time)

total_seconds = (hours * 3600) + (minutes * 60) + seconds + cook_time
hours = int(total_seconds / 3600)
minutes = int(total_seconds / 60) - (hours * 60)
seconds = total_seconds % 60
days = int(total_seconds / 86400)

if hours>=24:
    print(f"{hours-(days*24)} {minutes} {seconds}")
else:
    print(f"{hours} {minutes} {seconds}")

# hours, minutes, seconds = map(int, input().split())
# cook_time = int(input())  # 문자열을 정수로 변환

# total_seconds = (hours * 3600) + (minutes * 60) + seconds + cook_time
# hours = (total_seconds // 3600) % 24  # 24시간 단위로 조정
# minutes = (total_seconds // 60) % 60
# seconds = total_seconds % 60

# print(hours, minutes, seconds)
