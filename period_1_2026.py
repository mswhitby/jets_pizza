def calc_price(toppings):
    
    
    toppings_dict = {
        # key: value
        "T": 1.50, # tomatoes
        "O": 1.25, # onions
        "P": 3.50, # pineapple
        "M": 3.75, # mushrooms
        "A":  .40, # avocado
    }   
    
    print(toppings)
    toppings = set(toppings)
    print(toppings)
    
    base_price = 15
    
    for i in toppings:
        if i == "T":
            base_price += toppings_dict["T"]
            
        if i == "O":
            base_price += toppings_dict["O"]
        
        if i == "P":
             base_price += toppings_dict["P"]

        if i == "M":
            base_price += toppings_dict["M"]
            
        if i == "A":
            base_price += toppings_dict["A"]
            
            
            
    if base_price > 20:
        
        base_price *= .95
    
    base_price = round(base_price, 2)
        
        
        
            
    return base_price

    
    
            
    
    
toppings = "TPM"
print(calc_price(toppings))

toppings = "AAAAAAAMMTGTMMMXMMT"
print(calc_price(toppings))
