# define our pricing function
def pizza_price():
    
    # create a price dictionary
    price_dict = {
        
        # key: value,
        "T": 1.5,
        "O": 1.25,
        "P": 3.5,
        "M": 3.75,
        "A": .4,
    }
    
    # variable assignment
    base_price = 15
    
    # The variable "toppings" is assigned input value
    toppings = input("What toppings? ").upper()
    calculated_toppings_list = []
    
    for character in toppings:    
        
        if character in calculated_toppings_list:
            continue
        
        topping_price = price_dict.get(character)
        base_price = base_price + topping_price
        
        
        calculated_toppings_list.append(character)
        
            
    if base_price > 20:
        base_price = base_price * .95
        
    base_price = round(base_price, 2)   
    
    
    # print(f"The price of your pizza is, {base_price}!")
    print("The price of your pizza is, " + str(base_price) + "!")
    
pizza_price()
        