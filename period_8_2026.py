def calc_price(toppings):
    
    base_price = 15
    
    for t in toppings:
        
        # tomatoes
        if t == "T":
            base_price += 1.5 # Same as base_price = base_price + 1.5
            
        if t == "O":
            base_price += 1.25
            
        if t == "P":
            base_price += 3.50
            
        if t == "M":
            base_price += 3.75
            
        if t == "A":
            base_price += 0.40  
            
    # apply discount for orders over 20
    if base_price > 20:
        base_price *= .95
        
    base_price = round(base_price, 2)
            
            
    return base_price
            
    
    
toppings = "TPM"
print(calc_price(toppings))

toppings = "AAAAAAAMMTGTMMMXMMT"
print(calc_price(toppings))
