import dougUtility as dU
from objects import DDR4, DDR6


def ram_factory(amount, typeString):
    if typeString == "DDR4":
        return DDR4(amount)
    elif typeString == "DDR6":
        return DDR6(amount)
    else:
        return None


def main():
    ram_amounts = [8, 16, 32, 64, 128]
    ram_types = ["ddr4", "ddr6"]
    user_ram_amount = dU.getNumberFromChoices("Enter amount of RAM", ram_amounts, False)
    user_ram_type = dU.getNotEmptyStringFromChoices("\nEnter RAM type", ram_types)

    my_new_ram = ram_factory(user_ram_amount, user_ram_type)

    if isinstance(my_new_ram, DDR4):
        print("\nYou created a DDR4 object!\n")
    elif isinstance(my_new_ram, DDR6):
        print("\nYou created a DDR6 object!\n")
    else:
        print("\nYou created nothing\n")

    print((15*"="), "Bill Amount", (15*"="), "\nTotal cost for", my_new_ram.amount, "GB of", my_new_ram.type, "RAM is: $",my_new_ram.get_cost())


if __name__ == '__main__':
    main()

