from colorama import Fore, Style, init, Back

init(autoreset=True)
print(Back.RED + Fore.WHITE + "The Miles Per Gallon Program" + Style.BRIGHT)
print(Back.GREEN + Fore.WHITE + "Welcome to the program!")
print(Back.YELLOW + Fore.WHITE + "Enter your data below:")
print()

while True:
    miles_driven = float(input(Fore.GREEN + "Enter miles driven:\t\t"))
    gallons_used = float(input(Fore.GREEN + "Enter gallons of gas used:\t"))
    cost_per_gallon = float(input(Fore.GREEN + "Enter cost per gallon:\t\t"))

    if miles_driven <= 0:
        print("Miles driven must be greater than 0. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than 0. Please try again.")
    else:
        print()
        mpg = round(miles_driven / gallons_used, 2)
        print(Fore.YELLOW + "Miles Per Gallon:\t\t" + str(mpg))
        total_cost = round(gallons_used * cost_per_gallon, 2)
        print(Fore.YELLOW + "Total Cost of Gas:\t\t$" + str(total_cost))
        cost_per_mile = round(total_cost / miles_driven, 2)
        print(Fore.YELLOW + "Cost Per Mile:\t\t\t$" + str(cost_per_mile))

    another = input(Fore.GREEN + "Get entries for another trip? (y/n):\t")
    if another.lower() != "y":
        break

print()
print(
    Back.RED
    + Fore.WHITE
    + "Thank you for using the Miles Per Gallon Program"
    + Style.BRIGHT
)
