peter_budget = float(input())
number_videocards = int(input())
number_process = int(input())
number_ram = int(input())

price_videocard = 250
price_process = (price_videocard * number_videocards) * 0.35
price_ram = (price_videocard * number_videocards) * 0.1

total_amount = number_videocards * price_videocard + \
               number_process * price_process + \
               number_ram * price_ram
if number_videocards > number_process:
    total_amount *= 0.85

if peter_budget >= total_amount:
    print(f"You have {peter_budget - total_amount:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(total_amount - peter_budget):.2f} leva more!")