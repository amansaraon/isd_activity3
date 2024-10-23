"""
Description: The Observer class is an abstract base class that requires its subclasses to implement the update method for receiving notifications 
Author: ACE Faculty
Edited by: Amandeep Singh
Date: 20-10-2024
"""

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass
