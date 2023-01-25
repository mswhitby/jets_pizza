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
            
        if letter == "A":
            base_price = base_price + .40
            
        print(letter, base_price)
            
    if base_price > 20:
        base_price = base_price - (base_price *.05) 
        # base_price = base_price * .95
            
            
    return base_price
    
    
if __name__ == "__main__":
    print(price_pizza("AAAAAAAMMTGTMMMXMMT"))

    



