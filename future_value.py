#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from colorama import init, Fore, Back, Style
print("Welcome to the Future Value Calculator!")
print()

choice = "y"
while choice.lower() == "y":
    monthly_investment = float(input("Enter monthly investment:\t"))
    yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    years = int(input("Enter number of years:\t\t"))

    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

    print(f"Future value:\t\t\t{round(future_value, 2)}")
    print()

    choice = input("Continue? (y/n): ")

print("Bye!")