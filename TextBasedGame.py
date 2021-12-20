# Name: Joel De Alba
# Date: 12/15/21
# Course of Study: IT-140 Intro to Scripting

def main():

    print("\n\nWelcome to the Graveyard Skellies game")
    print("\nStory:\nYou have awoken in a Mausoleum Crypt, you don't remember who you are or why you are here.")
    print("You hear voices in your head, and are experiencing memory flashbacks of your past as")
    print("the  entire Mausoleum trembles, rocks and boulders fall, you see shinny black magic in the air.\n")
    print("Instructions:\nMove through the rooms to discover your past and survive by collecting all 6 items becoming "
          "stronger")
    print("You will not be able to beat the boss without all items collected.\n")
    print("Acceptable are North, South, West, or East")
    # A dictionary for the simplified dragon text game
    # The dictionary links a room to other rooms.
    rooms = {                                           # ~~ Dictionary created and organized on personal means
        'Resurrection Crypt': {                         # [0] ~~ Main Entrance Room w/ 0 items, room index 0 key
            'South': 'Family Paintings and Memorial Room'},  # Possible directions to travel for room index 0 value
        'Family Paintings and Memorial Room': {         # [1] ~~ Second Room w/ 1 item, room index 1 key
            'West': 'Weapons and Equipment Room',       # Possible directions to travel for room index 1 value
            'North': 'Resurrection Crypt',             # Possible directions to travel for room index 1 value
            'Item': 'Imperial Shard'},
        'Main Room - Weapons and Equipment Room': {     # [2] ~~ Third Room w/ 1 item, room index 2 key
            'North': 'Horsemen Crypt - War',            # Possible directions to travel for room index 2 value
            'West': 'Boss Room',                        # Possible directions to travel for room index 2 value
            'South': 'Horsemen Crypt - "Conquest',      # Possible directions to travel for room index 2 value
            'East': 'Family Paintings and Memorial Room',  # Possible directions to travel for room index 2 value
            'Item': 'Imperial Shield'},
        'Horsemen Crypt - "Conquest': {                 # [3] ~~ Fourth Room w/ 1 item, room index 3 key
            'East': 'Horsemen Crypt - "Famine"',        # Possible directions to travel for room index 3 value
            'North': 'Weapons and Equipment Room',     # Possible directions to travel for room index 3 value
            'Item': 'Shadow Power'},
        'Horsemen Crypt - "Famine': {                   # [4] ~~ Fifth Room w/ 1 item, room index 4 key
            'West': 'Horsemen Crypt - "Conquest',      # Possible directions to travel for room index 4 value
            'Item': 'Shadow Cloak'},
        'Horsemen Crypt - "War"': {                     # [5] ~~ Sixth Room w/ 1 item, room index 5 key
            'East': 'Horsemen Crypt - "Death"',         # Possible directions to travel for room index 5 value
            'South': 'Weapons and Equipment Room',     # Possible directions to travel for room index 5 value
            'Item': 'War Sword'},
        'Horsemen Crypt - "Death"': {                   # [6] ~~ Seventh Room w/ 1 item, room index 6 key
            'West': 'Horsemen Crypt - "War"',          # Possible directions to travel for room index 6 value
            'Item': 'Dark Magical Cloth'},
        'Boss Room': {                                  # [7] ~~ Eighth Room w/ 1 item, room index 7 key
            'East': 'Weapons and Equipment Room',      # Possible directions to travel for room index 7 value
            'West': 'Boss Room'},
        'Inventory': {                                      # [8] ~~ Items Room w/ All items, room index 8 key
            '"I" to return, ': 'Returns to Previous Room',
            '"V" to view current inventory': 'Displays Current Inventory Array'},
                                                        # [9] ~~ Exit Room w/ 0 items, room index 9 key
        'Exit Room': {'Start': 'Resurrection Crypt', 'Exit': 'Exit Game'},
    }
    game_options = {  # Creates another dictionary the prevents rooms
        'options': {  # dictionary from mixing with game options
            '"I" for inventory': 'Player Inventory,',
            '\nType "X" or type "Exit" to enter the Exit Screen': 'Exit Screen'}}

                                          # Creates user inventory of items
    rv = rooms.values()                                 # Stores dictionary values to variable
    rv_list = list(rv)                                  # Converts Dictionary values into list for easy use
    rk = rooms.keys()                                   # Stores dictionary keys to variable
    rk_list = list(rk)                                  # Converts Dictionary keys into list for easy use
    gv = game_options.values()                          # Stores dictionary values to variable
    gv_list = list(gv)                                  # Converts Dictionary values into list for easy use
    gk = game_options.keys()                            # Stores dictionary keys to variable
    gk_list = list(gk)                                  # Converts Dictionary keys into list for easy use
    keys = list(rooms)                                  # Stores and converts dictionary
    current_room = keys[0]                              # Sets the current room index to a variable
    next_room_location = rv_list[0]                     # Stores the dictionary room locations from the values
    options_menu = gv_list[0]                           # Sets the options_menu to the game_options dictionary
    r_items_count = 0                                   # Creates a placeholder for room that have already been entered
    rooms_count = 1
    p_items_count = 0                                   # Creates a placeholder for player amount of items
    inventory = []


    # Asks player if they would like to continue and tells them how to win
    p_direction = input('Press "enter" to Continue with game, or type "exit" to quit\n')
    # if player exits program ends, if not then loop begins
    while True:
        print('You are currently in:', current_room)  # prints current room name
        print("The available moves are:", *next_room_location)  # prints current available directions
        print('\nRoom Level Progression: |', str(rooms_count), '| Player Items: |', str(p_items_count), '|')

        # Asks player which direction they would like to go
        p_direction = input('Which direction or action would you like to take?\n').strip().capitalize()
        # checks which room the player is currently in, the first room is the "Resurrection Crypt

        ## ~~ Room 1 index[0] - Checks if player in room 1
        if current_room == keys[0]:
            if p_direction == "South": 
                if rooms_count == 1:      # if player input direction is correct by being inside the rooms
                    rooms_count += 1
                    current_room = keys[1]                  # dictionary?, then the current room becomes the next room by
                    next_room_location = rv_list[1]
                else:
                    current_room = keys[1]                  # dictionary?, then the current room becomes the next room by
                    next_room_location = rv_list[1]        # re-assigning the variables to the new library list index

            elif p_direction == 'I':                    # if user input is I proceeds to inventory menu as a room
                print('\nA shadow portal opens and swallows you, you have entered a a room of you collections!\n')
                current_room = keys[8]                  # if input is I, places player in inventory_room providing menu
                next_room_location = rv_list[8]         # if input is I, provides next available moves

            elif p_direction == 'Exit':                 # Gives the option to exit as nesting of if statements
                current_room = keys[9]                  # has eliminated,
                next_room_location = rv_list[9]
            else:                                           # If any other key is pressed, this else prints
                print('Sorry, you ran into a wall, Try Again!\n')

        ## ~~ Room 2 index[1] - Checks if player in room 2
        elif current_room == keys[1]:                    # Checks if correct room
        ## ~~ Room 2 index[1] - Checks if player in room 2

            if p_direction == 'West':                   # Checks for next room direction from user input
                if rooms_count <= 2:
                    rooms_count += 1
                    current_room = keys[2]
                    next_room_location = rv_list[2]
                else:
                    current_room = keys[2]
                    next_room_location = rv_list[2]

            elif p_direction == 'North':                 # Checks for next room direction from user input
                    current_room = keys[0]
                    next_room_location = rv_list[0]

            elif p_direction == 'Item':
                room_item = "Imperial Shard"
                if room_item not in inventory:
                    inventory.append(room_item)
                    p_items_count += 1
                    print('Item', inventory)

                else:
                    print('\nSorry! This item has already been collected!\n')

            elif p_direction == 'I':                    # if user input is I proceeds to inventory menu as a room
                print('\nA shadow portal opens and swallows you, you have entered a a room of you collections!\n')
                current_room = keys[8]                  # if input is I, places player in inventory_room providing menu
                next_room_location = rv_list[8]         # if input is I, provides next available moves

            elif p_direction == 'Exit':                 # if input is Exit, moves to exit room
                current_room = keys[9]                  # if input is Exit, sets current room to be exit room
                next_room_location = rv_list[9]         # if input is Exit, provides next available moves in exit room

            else:                                           # If any other key is pressed, this else prints
                print('Sorry, you ran into a wall, Try Again!\n')

        ## ~~ Room 3 index[2] - Checks if player in room 3
        elif current_room == keys[2]:

            if p_direction == 'North':
                if rooms_count <= 5:
                    rooms_count += 1
                    current_room = keys[5]
                    next_room_location = rv_list[5]
                else:
                    current_room = keys[5]
                    next_room_location = rv_list[5]

            elif p_direction == 'West':
                if p_items_count == 6:
                    current_room = keys[7]
                    next_room_location = rv_list[7]
                else:
                    print('Sorry! You cannot continue. Insufficient items to progress!')

            elif p_direction == 'South':
                if rooms_count <= 3:
                    rooms_count += 1
                    current_room = keys[3]
                    next_room_location = rv_list[3]
                else:
                    current_room = keys[3]
                    next_room_location = rv_list[3]

            elif p_direction == 'East':
                if rooms_count <= 3:
                    current_room = keys[1]
                    next_room_location = rv_list[1]
                else:
                    current_room = keys[1]
                    next_room_location = rv_list[1]

            elif p_direction == 'Item':
                room_item = "Imperial Shield"
                if room_item not in inventory:
                    p_items_count += 1
                    inventory.append(room_item)
                    print('Item', inventory)
                else:
                    print('\nSorry! This item has already been collected!\n')

            elif p_direction == 'I':                    # if user input is I proceeds to inventory menu as a room
                print('\nA shadow portal opens and swallows you, you have entered a a room of you collections!\n')
                current_room = keys[8]                  # if input is I, places player in inventory_room providing menu
                next_room_location = rv_list[8]         # if input is I, provides next available moves

            elif p_direction == 'Exit':
                current_room = keys[9]
                next_room_location = rv_list[9]
            else:  # If any other key is pressed, this else prints
                print('Sorry, you ran into a wall, Try Again!\n')

        # elif player in room 4 the if statement for direction
        elif current_room == keys[3]:

            if p_direction == 'East':
                if rooms_count <= 4:
                    rooms_count += 1
                    current_room = keys[4]
                    next_room_location = rv_list[4]
                else:
                    current_room = keys[4]
                    next_room_location = rv_list[4]

            elif p_direction == 'North':
                current_room = keys[2]
                next_room_location = rv_list[2]

            elif p_direction == 'Item':
                room_item = "Imperial Shield"
                if room_item not in inventory:
                    p_items_count += 1
                    inventory.append(room_item)
                    print('Item', inventory)
                else:
                    print('\nSorry! This item has already been collected!\n')

            elif p_direction == 'I':                    # if user input is I proceeds to inventory menu as a room
                print('\nA shadow portal opens and swallows you, you have entered a a room of you collections!\n')
                current_room = keys[8]                  # if input is I, places player in inventory_room providing menu
                next_room_location = rv_list[8]         # if input is I, provides next available moves

            elif p_direction == 'Exit':
                current_room = keys[9]
                next_room_location = rv_list[9]

            else:  # If any other key is pressed, this else prints
                print('Sorry, you ran into a wall, Try Again!\n')

        # elif player in room 5 the if statement for direction
        elif current_room == keys[4]:

            if p_direction == 'West':
                current_room = keys[3]
                next_room_location = rv_list[3]

            elif p_direction == 'Item':
                room_item = "Imperial Shield"
                if room_item not in inventory:
                    p_items_count += 1
                    inventory.append(room_item)
                    print('Item', inventory)
                else:
                    print('\nSorry! This item has already been collected!\n')

            elif p_direction == 'I':                # if user input is I proceeds to inventory menu as a room
                print('\nA shadow portal opens and swallows you, you have entered a a room of you collections!\n')
                current_room = keys[8]              # if input is I, places player in inventory_room providing menu
                next_room_location = rv_list[8]     # if input is I, provides next available moves

            elif p_direction == 'Exit':
                current_room = keys[9]
                next_room_location = rv_list[9]

            else:  # If any other key is pressed, this else prints
                print('Sorry, you ran into a wall, Try Again!\n')

        # elif player in room 6 the if statement for direction
        elif current_room == keys[5]:

            if p_direction == 'East':
                if rooms_count <= 5:
                    rooms_count += 1
                    current_room = keys[6]
                    next_room_location = rv_list[6]

            elif p_direction == 'South':
                    current_room = keys[6]
                    next_room_location = rv_list[6]

            elif p_direction == 'Item':
                room_item = "Imperial Shield"
                if room_item not in inventory:
                    p_items_count += 1
                    inventory.append(room_item)
                    print('Item', inventory)
                else:
                    print('\nSorry! This item has already been collected!\n'))

            elif p_direction == 'I':                    # if user input is I proceeds to inventory menu as a room
                print('\nA shadow portal opens and swallows you, you have entered a a room of you collections!\n')
                current_room = keys[8]                  # if input is I, places player in inventory_room providing menu
                next_room_location = rv_list[8]         # if input is I, provides next available moves

            elif p_direction == 'Exit':
                current_room = keys[9]
                next_room_location = rv_list[9]

            else:  # If any other key is pressed, this else prints
                print('Sorry, you ran into a wall, Try Again!\n')

        # elif player in room 7 the if statement for direction
        elif current_room == keys[6]:
            if p_direction == 'West':
                current_room = keys[5]
                next_room_location = rv_list[5]

            elif p_direction == 'Item':
                room_item = "Imperial Shield"
                if room_item not in inventory:
                    p_items_count += 1
                    inventory.append(room_item)
                    print('Item', inventory)
                else:
                    print('\nSorry! This item has already been collected!\n')

            elif p_direction == 'I':                    # if user input is I proceeds to inventory menu as a room
                print('\nA shadow portal opens and swallows you, you have entered a a room of you collections!\n')
                current_room = keys[8]                  # if input is I, places player in inventory_room providing menu
                next_room_location = rv_list[8]         # if input is I, provides next available moves

            elif p_direction == 'Exit':
                current_room = keys[9]
                next_room_location = rv_list[9]

            else:  # If any other key is pressed, this else prints
                print('Sorry, you ran into a wall, Try Again!\n')

        # elif player in room 8 the if statement for direction
        elif current_room == keys[7]:
            if p_direction == 'East':
                current_room = keys[5]
                next_room_location = rv_list[5]

            elif p_direction == 'West':
                current_room = keys[2]
                next_room_location = rv_list[5]

            elif p_direction == 'I':  # if user input is I proceeds to inventory menu as a room
                print('\nA shadow portal opens and swallows you, you have entered a a room of you collections!\n')
                current_room = keys[8]  # if input is I, places player in inventory_room providing menu
                next_room_location = rv_list[8]  # if input is I, provides next available moves

            elif p_direction == 'Exit':
                current_room = keys[9]
                next_room_location = rv_list[9]

            else:  # If any other key is pressed, this else prints
                print('Sorry, you ran into a wall, Try Again!\n')

        ## ~~ Inventory index[8] - Checks if player has accessed Inventory
        elif current_room == keys[8]:
            if p_direction == 'V':
                print('---------------------------------------------------------------------------------------')
                print('|', inventory, '|')
            if p_direction == 'I':  # if user input is I proceeds to inventory menu as a room
                # if input is I, provides next available moves
                print('\nA shadow portal opens and swallows you, you have returned to the Main Room\n')
                current_room = keys[2]
                next_room_location = rv_list[2]

            elif p_direction == 'Exit':  # Gives the option to exit as nesting of if statements
                current_room = keys[9]  # has eliminated,
                next_room_location = rv_list[9]
        else:
            exit()


main()

