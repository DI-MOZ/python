foods=[]
prices=[]
total=0

while True:
    food= input("enter a food to buy(q to quit): ")
    if food.lower()=="q":
       break
    else:
        price=float(input(f"enter the price of a {food}: ksh"))
        foods.append(food)
        prices.append(prices)


print("............your cart........")   

for food in foods:
    print(food)
for price in prices:
    total +=price
    print()
print(f"your total is : ksh {total}")
         
    
     
