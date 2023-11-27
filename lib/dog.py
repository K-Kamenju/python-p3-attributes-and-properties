#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name = None, breed = None):
        self._name = None
        self._breed = None

        self.name = name
        self.breed = breed

    def get_name(self):
        print("Retrieving Name")
        return self._name

    def set_name(self, name):
        if (type(name) == str) and 1 < len(name) < 25:
            self._name = name
            print(name)
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        print("Retrieving Breed")
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
            print(breed)
        else:
            print("Breed must be in the list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

# Test case
fido = Dog()
fido.name = "Alicia Keys"  # Valid name
fido.breed = "Pug"   # Valid breed

fido.name = 123      # Invalid name, prints: "Name must be a string between 1 and 25 characters."
fido.breed = "Labrador"  # Invalid breed, prints: "Breed must be in the list of approved breeds."
