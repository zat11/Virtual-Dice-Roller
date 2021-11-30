import random
print("Digital Dice Roller")
print("Developer: Zat Tech")
numbs= "1", "2", "3", "4", "5", "6"
print("To roll the dice, press r and enter!")
cmd=input()
if cmd == "r":
    lol=random.choice(numbs)
    print(lol)

