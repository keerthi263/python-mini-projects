#concession
menu={"popcorn":7.89,
      "cold coffee":5.67,
      "juice":3.45,
      "chicken burger":8.97}
cart=[]
total=0
print("--------------------------------")
print("             MENU                ")
print("---------------------------------")
for key,values in menu.items():
    print(f"{key:15}:${values}")
while True:
    food=input("Select a item:(q to quit):").lower()
    if food=="q":
        break
    else:
        cart.append(food)

print("---------YOUR ORDER----------")
for food in cart:
    total+=menu.get(food)
    print(food,end=" ")
    print()
print(f"your total is:${total:.2f}")

