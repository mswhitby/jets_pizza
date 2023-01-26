def price_pizza(toppings):
    
    # print(toppings)
    toppings = toppings.upper()
    # print(toppings)
    
    base_price = 15
    calculated_toppings_list = []
    
    for letter in toppings:
        
        if letter in calculated_toppings_list:
            continue
        
        if letter == "T":
            base_price = base_price + 1.5
            
        if letter == "O":
            base_price = base_price + 1.25
            
        if letter == "P":
            base_price = base_price + 3.50
            
        if letter == "M":
            base_price = base_price + 3.75
            
        if letter == "A":
            base_price = base_price + .40
            
        print(letter, base_price)
        calculated_toppings_list.append(letter)
            
    if base_price > 20:
        base_price = base_price - (base_price *.05) 
        # base_price = base_price * .95
            
            
    return round(base_price, 2)
    
    
if __name__ == "__main__":
    # print(price_pizza("AAAAAAAMMTGTMMMXMMT"))
    print(price_pizza("aaaaaammtgtmmmxmmt"))

    



