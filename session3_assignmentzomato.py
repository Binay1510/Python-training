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
print(message)

amount=int(input("Enter Order Amount:"))
promo_code=input("Enter Promo code ")

print("Amount: \u20b9 ",amount)
print("Promo Code ",promo_code)


if promo_code == "TRYNEW":
    if amount >= 149:
        discount = 0.30 * amount

        if discount > 75:
            discount = 75

        print("Discount is: \u20b9", discount)
        amount -= discount
        print("Please Pay: \u20b9", amount)
    else:
        print("Add items worth", (149-amount), "more")


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

