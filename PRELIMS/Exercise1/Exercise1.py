nintendo_price = 100
totalNintendo = 0
money = float(input("Enter your total money: "))
num_of_wii = int(money // nintendo_price)
remaining_money = money % nintendo_price
money_needed = float(nintendo_price - remaining_money)
print("You can purchase", num_of_wii, "Nintendo Wii")
print("You need", money_needed, "to purchase another Nintendo Wii")


