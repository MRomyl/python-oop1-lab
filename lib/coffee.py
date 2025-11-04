#!/usr/bin/env python3

class Coffee:
    valid_sizes = ["Small", "Medium", "Large"]
    def __init__(self, size, price):
        self.size = size
        self.price = price

        if size not in Coffee.valid_sizes:
            print("size must be Small, Medium, or Large")
    
    def tip(self):
        self.price =+ 1
        print("This coffee is great, here's a tip!")


    





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