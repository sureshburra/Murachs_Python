from colorama import Fore, Style, init, Back

init(autoreset=True)
print(Back.RED + Fore.WHITE + "The Miles Per Gallon Program"+ Style.BRIGHT)
print()

miles_driven = float(input(Fore.GREEN + "Enter miles driven:\t\t"))
gallons_used = float(input(Fore.GREEN +"Enter gallons of gas used:\t"))

if miles_driven <=0:
    print("Miles driven must be greater than 0. Please try again.")
elif gallons_used <=0:
    print("Gallons used must be greater than 0. Please try again.")
else:
    mpg = round(miles_driven / gallons_used, 2)
    print(Fore.YELLOW + "Miles Per Gallon:\t\t" + str(mpg))

print()
print(Back.RED + Fore.WHITE + "Thank you for using the Miles Per Gallon Program" + Style.BRIGHT)