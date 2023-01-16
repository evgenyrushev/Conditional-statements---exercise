from math import ceil
name_series = str(input())
episode_duration = int(input())
rest_duration = int(input())

lunch = rest_duration / 8
scrolling = rest_duration / 4

time_occupied = lunch + scrolling + episode_duration

if time_occupied <= rest_duration:
    print(f"You have enough time to watch {name_series} and left with {ceil(rest_duration - time_occupied)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_series}, you need {ceil(time_occupied - rest_duration)} more minutes.")
