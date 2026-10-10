"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# TODO: def show_status(current_room, inventory, room_items):
        print("You are in the {current_room}")
        print("Inventory: {inventory}")

# TODO: Create the gameplay loop required by the milestone.
# Within the loop, complete the required behavior in small steps:
#   1. while True:
          show_commands()
          show_status(current_room, inventory, rooms[current_room] ["item"])
#   2. player_input = input("Enter your move:").strip().lower().split()
       if len(player_input) == "exit"
            print("Thanks for playing!")
#   3. command = player_input[0]
        if command = "go":
            if len(player_input) < 2:
                print("Please choose a direction to move!")
                continue
          
#   4. direction = player_input[1].capitalize()
        if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
        else:
            print("No room that direction")
#   5. if current_room == "Villain room":
           if len(inventory) == required_items:
               print("Success! You have defeated the Dragon!")
           else:
               print("The Dragon ate you for dinner! Better luck next time!")
               break

      if __name__ == "__main__":
          main()

# TODO: Run and debug all milestone cases in prototype/README.md.
