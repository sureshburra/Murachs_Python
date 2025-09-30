#!/usr/bin/env python3
from colorama import Fore, Back, Style, init
from loguru import logger

init(autoreset=True)
print(Back.RED + Fore.GREEN+ "The Invoice Program")
print()

# logger.log("DEBUG", "This is a debug message")
# logger.info("This is a info message")
customer_type = input("Enter customer type (r/w):\t")
invoice_total = float(input("Enter invoice total:\t\t"))
print()

# determine discounts for Retail customers
if customer_type.lower() == "r":
    if invoice_total>0 and invoice_total<100:
        discount_percent = 0
    elif invoice_total>=100 and invoice_total<250:
        discount_percent = .1
    elif invoice_total>=250 and invoice_total<500:
        discount_percent = .2
    elif invoice_total>=500:
        discount_percent = .25
elif customer_type.lower() == "w":
    if invoice_total>0 and invoice_total<500:
        discount_percent = .4
    elif invoice_total>=500:
        discount_percent = .5
else:
    discount_percent = 0

discount_amount = round(invoice_total * discount_percent,2)
new_invoice_total = invoice_total - discount_amount

print(Fore.GREEN + f"Invoice total:\t\t${invoice_total:,.2f}")
print(Fore.GREEN + f"Discount percent:\t{discount_percent:.0%}")
print(Fore.GREEN + f"Discount amount:\t${discount_amount:,.2f}")
print(Fore.GREEN + f"New invoice total:\t${new_invoice_total:,.2f}")
print()
print(Fore.GREEN + "Bye!")
