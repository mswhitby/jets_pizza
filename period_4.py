# define a function
def pizza_price(toppings):
    
    # variable assignment
    # equal sign (=) - assignment
    base_price = 15
    
    for letter in toppings:
    
        # two equal signs (==) - equvilancy
        if letter == "T":
            base_price = base_price + 1.5
            
        if letter == "O":
            base_price = base_price + 1.25
            
        if letter == "P":
            base_price = base_price + 3.50
         
        if letter == "M":
            base_price = base_price + 3.75
            
        if letter == "A":
            base_price = base_price + 0.40
            
    if base_price > 20:
        base_price = base_price * 0.95
            
    return base_price
            

        
        

       
        
        
        
        
if __name__ == "__main__":
    toppings_input = input("What toppings?")
    print(pizza_price(toppings_input))
