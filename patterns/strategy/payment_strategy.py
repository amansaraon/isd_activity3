"""
Description: 
Author: ACE Faculty
Edited by: Amandeep Singh
Date: 20-10-2024
"""

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, account, payee, amount: float) -> str:
        """
        Process the payment for a specific billing account.
        Args:
            account (BillingAccount): The billing account to process payment for.
            payee (Payee): The payee associated with the payment.
            amount (float): The amount to be paid.
        Returns:
            str: Confirmation message of the payment processing result.
        """
        pass
    