# Project using dictionary and condition statement

menu={
    'pizza':50,
    'pasta':40,
    'Burger':75,
    'momos':45,
    'coffee':60,
}
#print(menu)

#Greet
print("Welcome to python resturant")
print("pizza:Rs.50\npasta:Rs40\nBurger:Rs75\ncoffee:Rs60\nmomos:Rs45")

order_total=0

item_1 = input("Enter the name of item as you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"order item {item_1} is not available yet!")

another_item = input("Do you want to add another order item? (Yes/No)")
if another_item == "Yes":
    item_2=input("Enter the name of second order item=")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"order item {item_2} is not available!")
    
print(f"The total amount of item to pay is {order_total}")






