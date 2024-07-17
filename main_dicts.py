import random
inventory = []

def start_game():
    print("welcome to lord of the dicts")
    print("You find yourself in a dark forest with two paths ahead.")
    print("TYpe 'cave' to explore the cave or 'river' to follow the river.")

    choice = input("What do you choose")
    if choice.lower() == 'cave':
        cave_path()
    elif choice.lower() == 'river':
        river_path()
    else:
        print("INvalid choice. Try again.") 
        exit()
        
def river_path():
    print("You follow the river and find a shiny dict lying on the ground")
    print("Type'dict' to pick up the dict or 'leave' to leave the massive dict")
    choice = input("What do you choose?")
    if choice.lower() == "dict":
        if 'dict' not in inventory:
            inventory.append('dict')
        else:
            print("You already have a sword.")
    elif choice.lower() == 'leave':
        print("You leave the dict behind.")
    else: 
        print("Invalid choice. try again.")
    print("there is no further path. You moved to the cave.")
    cave_path()      


def cave_path():
    print("You venture into the cave and find a sleeping dict lord")
    print("Type 'fight' to fight the sleeping dict lord or 'escape' from the cave.")
    choice = input("what do you choose")
    if choice.lower() == 'fight':
        if 'dict' in inventory:
            fight_dict_lord()
        else:
            print("You need a dict to fight the dict lord. Try to 'return'to the river to find the holy dict")
            cave_path()
    elif choice.lower() == 'river':
        print("you need return to the river of dicts")
        river_path()
    elif choice.lower() ==  'escape':
        print("You escape from the cave. You have -dict")
        game_over()
    else:
        print("invalid choice. try against.")
        cave_path()

def fight_dict_lord():
    print("You approach the dict lord with you 'average' but holy dict in hand")
    print("You attack the dict lord with you dict.")
    damage = random.randint(1,10)
    print("You dealt", damage, "with you dict against the dict lord")
    if damage == 9:
        print("you defeated the dict lord! congratulations you are the new lord of dicts")
        exit()
        #game_clear()
    else:
        print("The dict lord dominated you with his massive dicts! you are ripped open by his agressive thrusting. Game over!")
        game_over()
        
def game_over():
    print("game over. would like to play with mydicts again?")
    choice = input("Type 'yes' to play again or 'no to quit: ")
    if choice.lower() == 'yes':
        inventory=[]
        print("i apreciate you wanting to play with my dicts for a second time here you go")
        start_game()
    elif choice.lower() == 'no':
        print("most people can only handle my dicts once anyways")
        print("bye")
    else:
        print("Invalid choice. Try again.")
        game_over()
    
    

start_game()