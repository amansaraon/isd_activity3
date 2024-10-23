"""
Description: A client program written to verify correctness of 
the activity classes.
Author: ACE Faculty
Edited by: Amandeep Singh
Date: 20-10-2024
"""
from billing_account.billing_account import BillingAccount
from payee.payee import Payee
from payment.payment import Payment
from patterns.strategy.penalty_strategy import PenaltyStrategy
from patterns.strategy.partial_payment_strategy import PartialPaymentStrategy
from restaurant.chef import Chef
from restaurant.waiter import Waiter
from restaurant.restaurant import Restaurant

def strategy():
    print("STRATEGY PATTERN OUTPUT")

    # Given: Creates a BillingAccount object and 
    # adds the current balance owed for each utility.
    account = BillingAccount()
    account.add_balance(Payee.ELECTRICITY, 560.0)
    account.add_balance(Payee.INTERNET, 290.0)
    account.add_balance(Payee.TELEPHONE, 130.0)

    print("Initial Balances:")
    print(account, "\n")

    # 1. Create a Payment object with a PenaltyStrategy payment strategy.
    try:
        penalty_payment = Payment(PenaltyStrategy())
    except Exception as e:
        print(f"Error: {e}")

    # 2. Use the Payment object's pay_bill method to pay the ELECTRICITY bill with 
    # an amount that does not pay off the entire balance shown above - print the 
    # result of the pay_bill method.
    try:
        result = penalty_payment.pay_bill(account, Payee.ELECTRICITY, 275.0)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

    # 3. Create a Payment object with a PartialPaymentStrategy payment strategy.
    try:
        partial_payment = Payment(PartialPaymentStrategy())
    except Exception as e:
        print(f"Error: {e}")

    # 4. Use the Payment object's pay_bill method to pay the TELEPHONE bill with 
    # an amount that does not pay off the entire balance shown above - print the 
    # result of the pay_bill method.
    try:
        result = partial_payment.pay_bill(account, Payee.TELEPHONE, 80.0)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

    # 5. Using the Payment object created in step 3, make another payment for the 
    # TELEPHONE bill with an amount that pays off the remainder of the balance - print 
    # the result of the pay_bill method.
    try:
        result = partial_payment.pay_bill(account, Payee.TELEPHONE, 50.0)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

    # 6. Print the BillingAccount object to show the updated balances for each of the payees.
    print("\nUpdated Balances:")
    print(account)

def observer():
    print("OBSERVER PATTERN OUTPUT")
    
    # 1. Create a Restaurant object.
    restaurant = Restaurant()

    # 2. Create two Chef objects with names of your choice.
    chef_1 = Chef("Navaan Sandhu")
    chef_2 = Chef("Prem Dhillon")

    # 3. Create two Waiter objects with names of your choice.
    waiter_1 = Waiter("Arjan Dhillon")
    waiter_2 = Waiter("Karan Aujla")

    # 4. Print each of the Chef and Waiter objects.
    print(f"Chef 1: {chef_1}")
    print(f"Chef 2: {chef_2}")
    print(f"Waiter 1: {waiter_1}")
    print(f"Waiter 2: {waiter_2}\n")

    # 5. Attach one chef (of your choice) as a restaurant observer.
    restaurant.attach(chef_1)

    # 6. Attach one waiter (of your choice) as a restaurant observer.
    restaurant.attach(waiter_1)

    # 7. Add the following events:
    #    - New dish added to the menu: Grilled Cheese Sandwich.
    #    - Special promotion on desserts.
    #    - We are out of tomatoes!
    
    print("Event: New dish added to the menu: Grilled Cheese Sandwich.")
    restaurant.event("New dish added to the menu: Grilled Cheese Sandwich.")

    print("\nEvent: Special promotion on desserts.")
    restaurant.event("Special promotion on desserts.")

    print("\nEvent: We are out of tomatoes!")
    restaurant.event("We are out of tomatoes!")

    # Note: Only chef_1 and waiter_1 receive notifications as they were the ones attached.

if __name__ == "__main__":
    strategy()
    print("************************************")
    observer()
