import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add an item to the end of the list
        self.items.append(item)

    def dequeue(self):
        # Remove and return the first item in the list
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        # Look at the first item without removing it
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        # Check if the list has 0 items
        return len(self.items) == 0

    def select_and_announce_winner(self):
        if self.is_empty():
            return None
            
        # Randomly select a winner from the current list
        winner = random.choice(self.items)
        
        # Dequeue everyone up to and including the winner
        while not self.is_empty():
            removed_customer = self.dequeue()
            if removed_customer == winner:
                break
                
        return winner