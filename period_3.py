# define a function
def pizza_price(toppings):
    
    base_price = 15
    
    # use "for" loop to iterate through toppings
    
    for item in toppings:
        
        if item == "T":
            base_price = base_price + 1.5
            
        if item == "O":
            base_price = base_price + 1.25 
            
        if item == "P":
            base_price = base_price + 3.5
            
        if item == "M":
            base_price = base_price + 3.75
            
        if item == "a":
            base_price = base_price + .40
            
    print(base_price)
    
    
    
    
    
    
    
    

# ask user to input toppings
toppings = input("What toppings? ")
price = pizza_price(toppings)
    
    
    
    
    
