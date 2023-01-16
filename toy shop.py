trip_price = float(input())
number_puzzles = int(input())
number_talking_dolls = int(input())
number_teddy_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

puzzle_price = 2.60
talking_dolls_price = 3
teddy_bears_price = 4.10
minions_price = 8.20
truck_price = 2

total_amount = (number_trucks * truck_price +
                number_minions * minions_price +
                number_puzzles * puzzle_price +
                number_talking_dolls * talking_dolls_price +
                number_teddy_bears * teddy_bears_price)

ordered_toys = number_trucks + \
               number_minions + \
               number_puzzles + \
               number_teddy_bears + \
               number_talking_dolls

if ordered_toys >= 50:
    total_amount *= 0.75

rent = total_amount * 0.1
total_amount = total_amount - rent

if total_amount >= trip_price:
   print(f"Yes! {total_amount - trip_price:.2f} lv left.")
elif total_amount < trip_price:
   print(f"Not enough money! {abs(total_amount - trip_price):.2f} lv needed.")
