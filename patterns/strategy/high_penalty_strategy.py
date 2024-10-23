"""
Description: 
Author: ACE Faculty
Edited by: Amandeep Singh
Date: 20-10-2024
"""

from patterns.strategy.payment_strategy import PaymentStrategy

class HighPenaltyStrategy(PaymentStrategy):
    def process_payment(self, amount_due):
        penalty = 0.10 if amount_due > 1000 else 0.05
        total_amount = amount_due + (amount_due * penalty)
        print(f"High Penalty Strategy: The total amount due with penalty is ${total_amount:.2f}")
        return total_amount
