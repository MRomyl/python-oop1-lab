#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count: int):
        self.title = title
        self.page_count = page_count

        if not isinstance(page_count, int):
            print("page_count must be an integer")

    def turn_page(self):
        self.page_count += 1
        print("Flipping the page...wow, you read fast!")
    


"""
Create Feature Branch

Create Book class:
__init__:
title: Require user to input
page_count: Require user to input
Properties:
page_count:
Ensure it is an integer
if not print “page_count must be an integer”
Methods:
turn_page():
Will print “Flipping the page...wow, you read fast!

”"""