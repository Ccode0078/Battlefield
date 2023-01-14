'''
Welcome to the field of combat! To fight the ultimate Dragon, select any character to play as.
Different player characteristics can defeat the dragon.
To determine who deserves to be the best fighter, pick your fighter!
'''
# A Wizard player build
wizard = "Wizard"
wizard_hp = 70
wizard_damage = 150
# Elf player build
elf = "Elf"
elf_hp = 100
elf_damage = 100
 # Human player build
human = "Human"
human_hp = 150
human_damage = 20
# Dragon player build
dragon_hp = 300
dragon_damage = 50
#  -- Main Menu --
while True:
    print('1) Wizard')
    print('2) Elf')
    print('3) Human')

    player = input('hello user please pick character:')
    if (player == '1'):
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if (player == '2'):
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if (player == '3'):
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    print('Unkown character')
#       Display player you have chosen with attributes
print('you have chosen the character ', character)
print('health ', my_hp)
print('damage ', my_damage)
#       Battle between player(1, 2 or 3) against the dragon
while True:  
    dragon_hp = dragon_hp - my_damage       # The player hitpoints
    print("The ", character, 'damaged the Dragon! ')
    print("The " "dragon hitpoints are now: ", dragon_hp)

    if (dragon_hp == 0 or dragon_hp < 0):
        print("The Dragon has lost the battle ")
        break
    my_hp = my_hp - dragon_damage
    print("The " "Dragon strikes back at ", character)  # Dragon hitpoints
    print("The ", character, "hitpoints are now: ", my_hp)

    if (my_hp == 0 or my_hp < 0):
        print("The ", character, "has lost the battle ")
        break
