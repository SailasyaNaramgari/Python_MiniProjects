import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518 ") -  ● ┌ ─ ┐ │ └ ┘
# #using unicode character

dice_art = {

    #value will be tuple
    #these are tuples made of strings

    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘") ,
    2: ("┌─────────┐",
        "│    ●    │",
        "│         │",
        "│    ●    │",
        "└─────────┘") ,
    3: ("┌─────────┐",
        "│    ●    │",
        "│    ●    │",
        "│    ●    │",
        "└─────────┘") ,
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘") ,
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘") ,
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
dice_num = int(input("How many dices : "))

for i in range(dice_num):
    dice.append(random.randint(1, 6))

#To get dices VERTICALLY :
#for i in range(dice_num):
#   for j in dice_art.get(dice[i]):
#        print(j)

#To get dices HORIZONTALLY :
for i in range(5):
    for j in dice:
        print(dice_art.get(j)[i], end="")
    print()

for i in dice:
    total += i

print(f"Total : {total}")