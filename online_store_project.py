# a dictionary of available items 
available_items = {
    "Iphone 12": {
        "price": 700, 
        "quantity": 4,
        },
    "Iphone 12 Pro": {
        "price": 1000, 
        "quantity": 2,
        },
    "Iphone 12 Pro Max": {
        "price": 1200, 
        "quantity": 1,
        },

}

# 1. view available items and buy what he/she wants
# 2. view shopping cart which contains bought items
# 3. view the total price of the shopping cart
# 4. quit the program

# initilize cart as a dictionary
cart = {}

menu_message = """
====Choose an action to perform====

1. View available items
2. View Cart
3. View total price of cart
4. Quit
"""

# a) we need to make a loop to keep the program running until user quits
# b) print menu message

while True:
    print(menu_message)

    user_input = input("Choose a number: ")


    # get the use's choice
    # 1. if the user chose to view available items
        # a)print the available items
        # b) get the item the user wants to buy/purchase
        # c) add the bought/purchased item to the cart
    
    if user_input == "1":
        print("\n======Available products======\n")
        for index, item in enumerate(available_items, start=1):
            # get the item price
            item_price = available_items[item]["price"]
            # get the item quantity
            item_quantity = available_items[item]["quantity"]
            # check if item not available
            if item_quantity != 0:
                print(f"{index}. {item}: ${item_price} ")
            else:
                print(f"{index}. {item}: ${item_price} (Out Of Stock) ")
        # get the item the user wants to buy        
        item_number = int(input("\n=====Add a product to the cart=====\nChoose a number(Enter zero to go back): "))
        # get the order name from the item number
        if item_number not in [0, 1, 2, 3]:
           
            item_number = int(input("\n=====To add a product to the cart choose 1, 2, or 3. 0 to go back=====\n: "))
        if item_number == 0:
            continue
        order_name =  list(available_items.keys())[item_number-1]
        
        
        # check if the item is available
        if available_items[order_name]["quantity"] == 0:
            print(f"\nSorry {order_name} is out of stock!\n")
            continue

        # remove 1 from item quantity when added to the cart
        available_items[order_name]["quantity"] -= 1
        
        # get the order quantity using if statement
        # if order_name not in cart:
        #     order_quantity = 1
        # else:
        #     order_quantity += 1
        # get the order quantity using dictionary .get() method
        order_quantity = cart.get(order_name, {}).get("quantity", 0)
        order_quantity += 1
        
        # get the order price
        order_price = available_items[order_name]["price"] 

        # get order info
        order_info = {
            order_name: {
                "price": order_price, "quantity": order_quantity
            }
        }
        # add order info to the cart
        cart.update(order_info)
       
        
        print(f"\n{order_name} added to the cart succesfully!\n")
    # 2. if the user chose to view cart    
    elif user_input == "2":
        print("\n===The Cart===\n")
        if cart:        
            for item in cart:
                item_price = cart[item]["price"]
                item_quantity = cart[item]["quantity"]
                total_item_price = cart[item]["price"] * cart[item]["quantity"]
                print(f"{item}: ${item_price} x {item_quantity} \ntotal: {total_item_price}")
            grand_total = sum([item["price"] * item["quantity"] for item in cart.values()])   
            print(f"Grand total is: ${grand_total}") 
        # if cart is empty, print no items has been bought        
        else:
            print("The Cart is empty! Nothing was purchased! ")

              
    # 3. if the user chose to view total price
    elif user_input == "3":
        if cart:        
            for item in cart:
                item_price = cart[item]["price"]
                item_quantity = cart[item]["quantity"]
                total_item_price = cart[item]["price"] * cart[item]["quantity"]
               
            grand_total = sum([item["price"] * item["quantity"] for item in cart.values()])   
            print(f"\n===Total Price of Cart=== \nis: ${grand_total}") 
        # if cart is empty, print no items has been bought        
        else:
            print("Cart is empty! Nothing was purchased! ")

    # 4. if the user chose to exit the program/quit
    elif user_input == "4":
        print("\nThanks for shopping at Codezilla store\n")
        break
    # 5. if the user chose an invalid option
    else:
        print(f"{user_input} is not a valid input!\n\nEnter 1, 2, 3, or 4")
        
# if the cart contains items, print the cart
print("===The Cart===\n")
if cart:        
    for item in cart:
        item_price = cart[item]["price"]
        item_quantity = cart[item]["quantity"]
        # get the total price of each item in the cart
        total_item_price = cart[item]["price"] * cart[item]["quantity"]
        # print the total price
        print(f"{item}: ${item_price} x {item_quantity} \ntotal: {total_item_price}")
    # sum all items in the cart to get the total price of cart 
    grand_total = sum([item["price"] * item["quantity"] for item in cart.values()])   
    print(f"Total price of cart is: ${grand_total}") 
# if cart is empty, print no items has been bought        
else:
    print("Cart is empty! Nothing was purchased! ")


   
