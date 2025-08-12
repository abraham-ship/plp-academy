# control flows and functions
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        price = price - (price * .20)
        print(price)
    else:
        print(price)
    return price

price = int(input("Please enter the original price of item: "))
discount_percent = int(input("Please enter the discount percentage: "))

calculate_discount(price, discount_percent)