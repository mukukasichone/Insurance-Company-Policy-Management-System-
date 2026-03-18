#Policyholder demonstration to display the registration, payment processing, and details of policyholders and products.
from Policyholder import Policyholder
from product import Product
from payment import Payment

# Create products
product1 = Product("P001", "Health Insurance", 5000)
product2 = Product("P002", "Car Insurance", 3000)

# Create policyholders
p1 = Policyholder("Mukuka Sichone", "PH001")
p2 = Policyholder("John Banda", "PH002")

print(p1.register())
print(p2.register())

# Process payments
payment1 = Payment(p1, product1)
payment2 = Payment(p2, product2)

print(payment1.process_payment())
print(payment2.process_payment())

# Display details
p1.display_details()
p2.display_details()