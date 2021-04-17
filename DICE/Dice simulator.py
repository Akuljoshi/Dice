import random
print("This is a dice simulator:")
x = input(" ")

while x == "y":
    if x == "n":
        break
    
    number = random.randint(1,6)
    
    if number == 1:
        print("----------")
        print("|                |")
        print("|       0       |")
        print("|                |")
        print("----------")

    elif number == 2:
        print("----------")
        print("|                |")
        print("|     0  0     |")
        print("|                |")
        print("----------")

    elif number == 3:
        print("----------")
        print("|       0       |")
        print("|       0       |")
        print("|       0       |")
        print("----------")

    elif number == 4:
        print("----------")
        print("      0  0      ")
        print("                  ")
        print("      0  0      ")
        print("----------")

    elif number == 5:
        print("----------")
        print("      0  0      ")
        print("        0        ")
        print("      0  0      ")
        print("----------")

    else:
        print("----------")
        print("      0  0      ")
        print("      0  0      ")
        print("      0  0      ")
        print("----------")

    x = (input("Press enter 'y' to roll 'n' to exit:"))
    







'''
import random

print("press enter to roll:")
number = random.randint(1,6)

if number == 1:
    print("----------")
    print("        0        ")
    print("        0        ")
    print("        0        ")
    print("----------")

elif number == 2:
    print("----------")
    print("   0000000 ")
    print("       000     ")
    print("      00        ")
    print("   0000000 ")
    print("----------")

elif number == 3:
    print("----------")
    print("        0        ")
    print("        0        ")
    print("        0        ")
    print("----------")

elif number == 4:
    print("----------")
    print("      0  0      ")
    print("                  ")
    print("      0  0      ")
    print("----------")

elif number == 5:
    print("----------")
    print("      0  0      ")
    print("        0        ")
    print("      0  0      ")
    print("----------")

else:
    print("----------")
    print("      0  0      ")
    print("      0  0      ")
    print("      0  0      ")
    print("----------")
    
    
'''
    
    
