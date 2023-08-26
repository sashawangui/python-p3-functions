#!/usr/bin/env python3

def greet_programmer():
    pass
    print ("Hello, programmer!")

def greet(name):
    pass
    print ("Hello, " + name + "!")

def greet_with_default(name="programmer"):
    pass
    print ("Hello, " + name + "!")

def add(num1, num2):
    pass
    return num1 + num2


def halve(number):
    pass
    if isinstance(number, (int, float)):
        return number / 2
    else:
        return None


