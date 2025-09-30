#!/usr/bin/env python3

from colorama import Fore, Back, Style, init
from loguru import logger

init(autoreset=True)
print(Fore.RED + "Enter 'exit' when you're done.\n")
while True:
    data = input("Enter an integer to square:\t")
    if data == "exit":
        break
    i = int(data)
    print(Fore.GREEN + f"{i} squared is {i**2}\n")

print(Fore.LIGHTGREEN_EX + "Okay, bye!")