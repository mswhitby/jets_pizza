def price_pizza(toppings):
    
    base_price = 15
    
    for letter in toppings:
        
        if letter == "T":
            
            base_price = base_price + 1.5
            
        if letter == "O":
            base_price = base_price + 1.25
            
        if letter == "P":
            base_price = base_price + 3.50
            
        if letter == "M":
            base_price = base_price + 3.75
            
        if letter == "a":
            base_price = base_price + .40

    



