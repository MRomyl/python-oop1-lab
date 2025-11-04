#!/usr/bin/env python3

class Coffee:
    valid_sizes = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        self._size = None
        self.size = size 
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in Coffee.valid_sizes:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1


    





"""
__init__:
size: Require user to input
price: Require user to input
Properties:
Size
Ensure size is either Small, Medium, or Large
If not print “size must be Small, Medium, or Large”
Methods:
tip():
Will print “This coffee is great, here’s a tip!”
Will increase price by 1 

"""