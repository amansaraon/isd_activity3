"""
Description: 
Author: ACE Faculty
Edited by: Amandeep Singh
Date: 20-10-2024
"""

from patterns.observer.observer import Observer

class Dishwasher(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Message to dishwasher {self.name}: {message}")
