movie_budget = float(input())
number_static = int(input())
clothing_price = float(input())

decor = movie_budget * 0.1

if number_static > 150:
    clothing_price *= 0.9

price_for_clothing_static = clothing_price * number_static

final_amount = price_for_clothing_static + decor

if movie_budget < final_amount:
    print("Not enough money!")
    print(f"Wingard needs {final_amount - movie_budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - final_amount:.2f} leva left.")