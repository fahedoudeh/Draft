# available items

pizzas = {
    "Margherita": 100, 
    "Pepperoni": 120,
    "Meat Lovers": 150, 
    "Chicken": 130
    }
burgers = {
    "Beef": 100, 
    "Chicken": 80, 
    "Bacon": 120
    }
drinks = {
    "Coke": 30, 
    "Sprite": 25, 
    "Fanta": 25, 
    "Pepsi": 30
    }
soups = {
    "Chicken Soup": 50, 
    "Beef Soup": 60,
    "Mushroom Soup": 40
    }
desserts = {
    "Ice Cream": 50, 
    "Chocolate Cake": 60,
    "Cheese Cake": 70
    }

# welcome message 
print("Welcome to Codezilla Resturant")
menu_message = """
1. Pizzas
2. Burgers
3. Drinks
4. Soups
5. Desserts
"""

options = """
==Choose an option==
1. Add another item
2. View the order
3. Clear the order
4. Exit
"""
        
order = {}

# make a while loop
while True:
    print(menu_message)
    # ask user for an input to choose 1 of the menu catigories 
    category_num = input("Please, Enter the number of the category you want: (press Enter to exit): ")
    # exit if user presses Enter
    if category_num == "":
        print("Thank you for visiting Codezilla resturant!")
        break
    # 1. pizzas
    elif category_num == "1":
        # enumerate pizzas dict
        for i, (pizza, price) in enumerate(pizzas.items(), start=1):
            # print the available pizzzas
            print(f"{i}.{pizza}: {price} EGP")
        # take pizza number from user    
        pizza_choice_number = int(input("Please, Enter the number of the pizza you want (0 to return to previous menu): "))
        
        # go back to the previous menu when user enters 0
       
        if pizza_choice_number not in [0, 1, 2, 3, 4]:
            pizza_choice_number = int(input("Number must be between 1 and 4 (0 for previous menu): "))
        elif pizza_choice_number == 0:
            continue    
        # make a list of the names of pizzas assign the pizza number as an index to match the pizza name 
        pizza_choice_name = list(pizzas.keys())[pizza_choice_number - 1]
        # determine pizza price
        pizza_price = pizzas[pizza_choice_name]
        # get the desired pizza quantity
        quantity_choice = int(input(f"how many {pizza_choice_name} pizzas do you like to order: "))
        # make pizza order info dict and add it to order dict
        pizza_order_info = {
            f"{pizza_choice_name} pizza": {"price": pizza_price, "quantity": quantity_choice}
        }

        order.update(pizza_order_info)

        # print further options menu
        print(options)
        # take the user choice
        option_choice_number = input("Please, Enter your choice: ")
        # 1. add another item. go back to the categories menu
        if option_choice_number == "1":
            continue
        # 2. view the order
        if option_choice_number == "2":
           print(order)
        # 3. clear the order
        # 4. exit

    # 2. burgers
    elif category_num == "2":
        # enumerate burgers dict
        for i, (burger, price) in enumerate(burgers.items(), start=1):
            # print the available burgers
            print(f"{i}.{burger}: {price} EGP")
        # take burger number from user    
        burger_choice_number = int(input("Please, Enter the number of the burger you want (0 to return to previous menu): "))
        # go back to the previous menu when user enters 0
        if burger_choice_number not in [0, 1, 2, 3, ]:
            burger_choice_number = int(input("Number must be between 1 and 3 (0 for previous menu): "))
        elif burger_choice_number == 0:
            continue   
        # make a list of the names of burgers assign the burger number as an index to match the burger name 
        burger_choice_name = list(burgers.keys())[burger_choice_number - 1]
        # determine burger price
        burger_price = burgers[burger_choice_name]
        # get the desired burger quantity
        quantity_choice = int(input(f"how many {burger_choice_name} burgers do you like to order: "))
        # make burger order info dict and add it to order dict
        burger_order_info = {
            f"{burger_choice_name} burger": {"price": burger_price, "quantity": quantity_choice}
        }

        order.update(burger_order_info)
    # 3. drinks
    # 4. soups
    # 5. desserts
    

        # print further options menu
        print(options)
        # take the user choice
        option_choice_number = input("Please, Enter your choice: ")
        # force a valid input
        if option_choice_number not in ['1', '2', '3', '4']:
            option_choice_number = (input("Number must be between 1 and 4: "))
          
        # 1. add another item. go back to the categories menu
        if option_choice_number == "1":
            continue
        # 2. view the order
        if option_choice_number == "2":
            if order:
                for item in order:
                    item_price = order[item]["price"]
                    item_quantity = order[item]["quantity"]
                    total_item_price = item_price * item_quantity
                    print(f"{item}: {item_price} EGP x {item_quantity} = {total_item_price}")

                total_order_price = sum([item["price"] * item["quantity"] for item in order])
                print(f"Total order: {total_order_price}")    
        # 3. clear the order
        # 4. exit

    




