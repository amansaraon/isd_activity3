"""
Description: 
Author: ACE Faculty
Edited by: Amandeep Singh
Date: 20-10-2024
"""

from patterns.strategy.payment_strategy import PaymentStrategy

class InterestPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount_due):
        interest_rate = 0.05  # 5% interest rate
        total_amount = amount_due + (amount_due * interest_rate)
        print(f"Interest Payment Strategy: The total amount due with interest is ${total_amount:.2f}")
        return total_amount
