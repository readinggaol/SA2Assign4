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
    user_ram_type = dU.getNotEmptyStringFromChoices("Enter RAM type", ram_types)

    my_new_ram = ram_factory(user_ram_amount, user_ram_type)

    if isinstance(my_new_ram, DDR4):
        print("You created a DDR4 object!")
    elif isinstance(my_new_ram, DDR6):
        print("You created a DDR6 object!")
    else:
        print("You created nothing")

    print("Total cost for ", my_new_ram.amount, " of ", my_new_ram.type, " ram is : ", my_new_ram.get_cost())


if __name__ == '__main__':
    main()

