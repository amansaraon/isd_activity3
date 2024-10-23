"""
Description: 
Author: ACE Faculty
Edited by: Amandeep Singh
Date: 20-10-2024
"""

from patterns.observer import Observer

class Waiter(Observer):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Waiter: {self.name}"

    def update(self, message):
        print(f"Message to waiter {self.name}: {message}")
