
mc_donalds_menu=[
    {
        "name":"burger",
        "price": 100,
        "quantity": 0
    },
    {
        "name": "fries",
        "price": 70,
        "quantity": 0
    },
    {
        "name": "coke",
        "price": 50,
        "quantity": 0
    },
    {
        "name": "pizza",
        "price": 300,
        "quantity": 0
    },
    {
        "name": "noodles",
        "price": 200,
        "quantity": 0
    }
]
message = """
    Welcome to Zomato
    Apply Promo Code
    -------
    TRYNEW
    -------
    Get 30% OFF up to ₹75
    Valid on total value of items worth ₹149 or more.

    -------
    ZOMATO
    -------
    FLAT 100 OFF
     Valid on total value of items worth ₹249 or more.

    -------
    ICICITREATS
    -------
    Get  credits worth ₹100 using ICICI Bank Credit cards
    Valid on total value of items worth ₹599 or more
"""



def shopping_cart():
    cart=[]
    total_amount=0
    total_dishes=0



    choice="yes"

    while choice=="yes":
        dish_name=input("enter dish name")

        for idx in range(len(mc_donalds_menu)):
            if mc_donalds_menu[idx]["name"]==dish_name:
                quantity=int(input("enter the dish quantity for "+dish_name+":"))
                mc_donalds_menu[idx]["quantity"]=quantity
                total_dishes+=quantity
                total_amount+=quantity*mc_donalds_menu[idx]["price"]
                cart.append(mc_donalds_menu[idx])
                break

        choice=input("do you wish to continue? yes/no")

    print("CART [", len(cart), "]")
    print(cart)
    print("Total Dishes:", total_dishes)
    print("Please Pay: \u20b9:", total_amount)



    print(message)

    amount = total_amount
    promo_code = input("Enter Promo code ")

    print("Amount: \u20b9 ", amount)
    print("Promo Code ", promo_code)

    if promo_code == "TRYNEW":
        if amount >= 149:
            discount = 0.30 * amount

            if discount > 75:
                discount = 75

            print("Discount is: \u20b9", discount)
            amount -= discount
            print("Please Pay: \u20b9", amount)
        else:
            print("Add items worth", (149 - amount), "more")


    elif promo_code == "ZOMATO":
        if amount >= 249:
            print("ZOMATO Applied Successfully")
            print("Please Pay: \u20b9", amount - 100)
        else:
            print("Please Pay: \u20b9", amount)



    elif promo_code == "ICICITREATS":
        if amount >= 599:
            print("ICICITREATS Applied Successfully")
            print("Please Pay: \u20b9", amount - 100)
            print("Congtas you recieved credits worth ₹100 using ICICI Bank Credit card")
        else:
            print("Please Pay: \u20b9", amount)

    else:
        print("Promo Code is Invalid")
        print("Please Pay: \u20b9", amount)


    return total_amount


result=shopping_cart()
