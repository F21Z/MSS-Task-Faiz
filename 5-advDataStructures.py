#Creating a dictionary named customer_info
customer_info = {
    'name': 'Severus Snape',
    'age': '38',
    'purchase history': ['Sword of Gryffindor', 'Nimbus 2024', 'The Elder Wand']
}

# Retrieving and printing the customer's name
customer_name = customer_info['name']
print(f"Customer Name: {customer_name}")

# Retrieving and printing second purchase
purchase_history = customer_info['purchase history']
if len(purchase_history) >= 2:
    second_purchase = purchase_history[1]
    print(f"Second Purchase: {second_purchase}")
else:
    print("Customer has not made a second purchase yet.")