print("Welcome to the Treasure Isalnd, Your missions is to find the treasure")


direction = input('Type left or right ').lower()

if direction == 'left':
    cross = input("You have come to a river.\n Do you want to wait for a boat or swim across ").lower()
    if cross == 'wait':
        door = input("You have arrived at the island.\n Which door do you want to go through: Red, Blue, Yellow ").lower()
        if door ==  'Red' or door == 'Blue':
            print('Game over')
        else:
            print('You win')
    else:
        print('Game Over') 
else:
    print('Game Over')