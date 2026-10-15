toppings = "TPM"

def calc_price(toppings):
    toppings_dict = {
        # key: value
        "T": 1.50, # tomatoes
        "O": 1.25, # onions
        "P": 3.50, # pineapple
        "M": 3.75, # mushrooms
        "A":  .40, # avocado
    }   
    
    base_price = 15
    
    for i in toppings:
        if i == "T":
            base_price += toppings_dict["T"]
            
        if i == "O":
            base_price += toppings_dict["O"]

    
    
