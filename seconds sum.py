import math

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_third + time_second + time_first

mintues = total_time // 60
seconds = total_time % 60

mintues = math.floor(mintues)

if seconds < 10:
    print(f"{mintues}:0{seconds}")
else:
    print(f'{mintues}:{seconds}')



