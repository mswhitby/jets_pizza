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
    print(toppings)
    toppings = set(toppings)
    print(toppings)
    
    for character in toppings:    
        
        topping_price = int(price_dict.get(character, 0))
        base_price = base_price + topping_price
        
            
    if base_price > 20:
        base_price = base_price * .95
        
    base_price = round(base_price, 2)   
    
    
    # print(f"The price of your pizza is, {base_price}!")
    print("The price of your pizza is, " + str(base_price) + "!")
    
pizza_price()
        