import random

class RandomizedSet:
    def __init__(self):
        # Initialize a list to store the elements and a dictionary to map element values to their indices in the list
        self.list = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        # Check if the value is already in the set (dict)
        if val in self.dict:
            return False  # Return false if the value is already present

        # Add the value to the list and store its index in the dict
        self.list.append(val)
        self.dict[val] = len(self.list) - 1
        print(dict[val], "->", len(self.list) - 1)
        return True  # Return true indicating successful insertion

    def remove(self, val: int) -> bool:
        # Check if the value is in the set (dict)
        if val not in self.dict:
            return False  # Return false if the value is not present

        # Swap the value with the last element in the list for efficient removal
        last_element = self.list[-1]
        idx = self.dict[val]
        self.list[idx], self.list[-1] = self.list[-1], self.list[idx]
        self.dict[last_element] = idx

        # Remove the value from the list and dict
        self.list.pop()
        del self.dict[val]
        return True  # Return true indicating successful removal

    def getRandom(self) -> int:
        # Return a random element from the list
        return random.choice(self.list)
