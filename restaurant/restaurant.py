"""
Description: 
Author: ACE Faculty
Edited by: Amandeep Singh
Date: 20-10-2024
"""

from patterns.observer.subject import Subject

class Restaurant(Subject):
    def __init__(self):
        super().__init__()
        self.message = ""

    def event(self, message):
        self.message = message
        self.notify(self.message)
