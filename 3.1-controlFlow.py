#defining the function
def calculate_discount(original_price, discount_percentage=10):
    discounted_price = original_price*(1-(discount_percentage/100))            #calculating discount
    return discounted_price

#testing from fixed input
#print(calculate_discount(1950))
#print(calculate_discount(1950,50))

#from input
while 1:
    price = input("Enter Original Price: $")
    if price=="":
        break                                                                  #exit loop if price not entered
    disc_percent = input("Enter discount percentage: ")
    if disc_percent=="":
        disc_price = calculate_discount(int(price))                            #calling function using default discount of 10%
    else:
        disc_price = calculate_discount(int(price), int(disc_percent))         #calling function using given discount
    print("Discounted Price = $",disc_price)                                   #print discounted price
    
    if disc_price <= 50:
        print("Low-cost item")
    elif 50 < disc_price <= 100:
        print("Moderate-cost item")
    elif disc_price > 100:
        print("High-cost item")