# define our pricing function
def pizza_price():
    
    # variable assignment
    base_price = 15
    
    # The variable "toppings" is assigned input value
    toppings = input("What toppings? ")
    
    for character in toppings:
        
        # equivalency
        if character == "T":
            base_price = base_price + 1.5
            
        if character == "o":
            base_price = base_price + 1.25
        
        if character == "P":
            base_price = base_price + 3.50
            
        if character == "M":
            base_price = base_price + 3.75
        
        if character == "A":
            base_price = base_price + .40
            
    if base_price > 20:
        base_price = base_price * .95
            
        
    base_price = round(base_price, 2)   
    print(base_price)
    
pizza_price()
        
