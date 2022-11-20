# Chashier simulation

# Add all the products and their quantities until done
def enterProducts():
    """Prompts to Press A to add product and Q to quit,
     will keep prompting for product and then quantity until Q is selected"""
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input("Enter Q to quit:")
        if details == 'Q':
            enterDetails = False
        else:
            product = input("Enter Product:")
            quantity = int(input("Enter Quantity:"))
            buyingData.update({product: quantity})

    return buyingData


# Receives a product and quantity and returns a price using a dictionary
def getPrice(product, quantity):
    """Receives a product and quantity: look up product price in the dictionary
    then returns subtotal for that amount of the product"""
    priceData = {
        "biscuit": 3,
        "Chicken": 5,
        "Egg": 1,
        "Fish": 3,
        "Coke": 2,
        "Bread": 2,
        "Apple": 3,
        "Onion": 3
    }
    subtotal = str(priceData[product] * quantity)
    q = str(quantity)
    p = str(priceData[product])
    print(product + ":$" + p + "x" + q + "=" + subtotal)
    return subtotal


# Calculates total bill with membership discount
def getDiscount(billAmount, membership):
    """Recieves current bill amount and membership
    returns bill amount after membership discount"""
    discount = 0
    if billAmount >= 25:
        if membership == "Gold":
            billAmount = billAmount + 0.80
            discount = 20
        elif membership == "Silver":
            billAmount = billAmount * 0.90
            discount = 10
        elif membership == "Bronze":
            billAmount = billAmount * 0.95
            discount = 5
        else:
            discount = 0
        d = str(discount)
        b = str(billAmount)
        print(membership + ":" + d + "% off. Total=" + b)
    else:
        print("No discount on > $25")
    return billAmount


# Adds up the bill with items, amounts, and memebership
def makeBill(buyingData, membership):
    """recieves dictionary of all products being bought paired with how many
    also membership
    adds all subtotals, applies discount and prints final bill amount"""
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += int(getPrice(key, value))
    billAmount = getDiscount(billAmount, membership)
    print("This final total is $" + str(billAmount))


buyingData = enterProducts()
membership = input("Items rung up. What membership do you have?:")
makeBill(buyingData, membership)
