"""
Description: 
Author: ACE Faculty
Edited by: Amandeep Singh
Date: 20-10-2024
"""

from patterns.strategy.payment_strategy import PaymentStrategy
from payee.payee import Payee
from billing_account.billing_account import BillingAccount  

class PenaltyStrategy(PaymentStrategy):
    """
    Implements a payment strategy that adds a penalty fee if the payment
    is insufficient to cover the balance.

    Methods:
        process_payment(account: BillingAccount, payee: Payee, amount: float) -> str:
            Deducts the payment amount from the account's balance for a given payee.
            If the balance is not fully paid off, adds penalty fee to the account.
    """
    def process_payment(self, account: BillingAccount, payee: Payee, amount: float) -> str:
        """
        Processes the payment with a penalty fee for insufficient payment.

        Args:
            account (BillingAccount): The billing account to process payment for.
            payee (Payee): The payee associated with the payment.
            amount (float): The amount to be paid.

        Returns:
            str: A confirmation message indicating whether the payment was sufficient
            or if a penalty fee was added.
        """
        
        account.deduct_balance(payee, amount)

        
        balance = account.get_balance(payee)

        if balance <=0:
            return f"Processed payment of ${amount:.2f}. New balance: ${balance:.2f}."
        else:
            account.add_balance(payee, 10.00)  
            return f"Insufficient payment. Added penalty fee of $10.00. New balance: ${balance:.2f}."
