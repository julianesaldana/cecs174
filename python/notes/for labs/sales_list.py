list_customers = []
list_purchases = []
customer = input("What is the name of the customer? ")
while customer != "":
    purchase = input("What is the purchase amount (numbers only)? ")
    while not purchase.isdigit():
        purchase = input("What is the purchase amount (numbers only)? ")
    purchase = int(purchase)
    if customer not in list_customers:
        list_customers.append(customer)
        list_purchases.append(purchase)
    else:
        position = list_customers.index(customer)
        list_purchases[position] += purchase
    customer = input("What is the name of the customer? ")

purchase_position = list_purchases.index(max(list_purchases))
highest_purchase = max(list_purchases)
highest_customer = list_customers[purchase_position]
print("%s spent $%d" % (highest_customer, highest_purchase))
