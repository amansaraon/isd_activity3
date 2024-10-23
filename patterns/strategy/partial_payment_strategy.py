"""
Description: 
Author: ACE Faculty
Edited by: Amandeep Singh
Date: 20-10-2024
"""

from patterns.strategy.payment_strategy import PaymentStrategy
from payee.payee import Payee
from billing_account.billing_account import BillingAccount

class PartialPaymentStrategy(PaymentStrategy):
    """
    Implements a payment strategy that allows partial payments without adding
    a penalty fee.

    Methods:
        process_payment(account: BillingAccount, payee: Payee, amount: float) -> str:
            Deducts the payment amount from the account's balance for a given payee.
            
    """
    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
    
        """
        Processes a partial payment for a given billing account and payee.

        Args:
            account (BillingAccount): The billing account to process payment for.
            payee (Payee): The payee associated with the payment.
            amount (float): The amount to be paid.

        Returns:
            string: A confirmation message indicating whether the balance was fully paid off
            or if the partial payment was accepted.
        """
        
        account.deduct_balance(payee, amount)

        balance = account.get_balance(payee)

        if balance <=0:
            return f"Processed payment of ${amount:.2f}. New balance: ${balance:.2f}."
        else:
            return f"Partial payment of ${amount:.2f} accepted. New balance: ${balance:.2f}."
