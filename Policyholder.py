# impliment methods for registering, suspending, and reactivating policyholders
class Policyholder:
    def __init__(self, name, policy_id):
        self.name = name
        self.policy_id = policy_id
        self.is_active = True
        self.products = [] 

    def register(self):
        return f"{self.name} registered successfully."

    def suspend(self):
        self.is_active = False
        return f"{self.name}'s policy is suspended."

    def reactivate(self):
        self.is_active = True
        return f"{self.name}'s policy is active again."

    def add_product(self, product):
        self.products.append(product)

    def display_details(self):
        status = "Active" if self.is_active else "Suspended"
        product_names = [p.name for p in self.products]

        print("\n----------------------------")
        print(f"Name: {self.name}")
        print(f"Policy ID: {self.policy_id}")
        print(f"Status: {status}")
        print(f"Products: {product_names}")
        print("----------------------------")