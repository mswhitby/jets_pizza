# define a function
def pizza_price(toppings):
    
    toppings = toppings.upper()
    print(toppings)
    
    base_price = 15
    calculated_toppings_list = []
    
    # use "for" loop to iterate through toppings
    for item in toppings:
        
        if item in calculated_toppings_list:
            continue
        

        if item == "T":
            base_price = base_price + 1.5
            
        if item == "O":
            base_price = base_price + 1.25 
            
        if item == "P":
            base_price = base_price + 3.5
            
        if item == "M":
            base_price = base_price + 3.75
            
        if item == "A":
            base_price = base_price + .40
            
        calculated_toppings_list.append(item)
            
    # Apply 5% if more than $20
    if base_price > 20:
        base_price = base_price * .95
        
        
    base_price = round(base_price, 2)

    print(base_price)
    
        
    
    
    
    
    
    

# ask user to input toppings
toppings = input("What toppings? ")
price = pizza_price(toppings)
