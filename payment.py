#impliment methods for processing payments, sending reminders, and applying penalties
from datetime import datetime
class Payment:
    def __init__(self, policyholder, product):
        self.policyholder = policyholder
        self.product = product
        self.amount = product.price
        self.date = None
        self.is_paid = False

    def process_payment(self):
        if not self.policyholder.is_active:
            return "Payment failed: Policyholder is suspended."

        self.is_paid = True
        self.date = datetime.now()
        self.policyholder.add_product(self.product)

        return f"Payment of {self.amount} successful for {self.policyholder.name}"

    def send_reminder(self):
        if not self.is_paid:
            return f"Reminder: {self.policyholder.name}, you have a pending payment."
        return "No reminder needed."

    def apply_penalty(self, penalty_amount):
        if not self.is_paid:
            self.amount += penalty_amount
            return f"Penalty applied. New amount: {self.amount}"
        return "No penalty needed."