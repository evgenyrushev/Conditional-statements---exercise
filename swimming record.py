record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_meter = float(input())

water_resistence = (distance_in_meters // 15)
water_resistence = water_resistence * 12.5

time_ivan = distance_in_meters * time_per_meter + water_resistence

if time_ivan < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {time_ivan:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(record_in_seconds - time_ivan):.2f} seconds slower.")