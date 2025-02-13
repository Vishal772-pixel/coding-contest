import random

# Defining  the grid size
GRID_SIZE = 5


def display_grid(player_pos):
   
    grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    # Place the player on the grid
    grid[player_pos[0]][player_pos[1]] = "P"  # P for Player
  
    for row in grid:
        print(" ".join(row))
    print()


def check_for_treasure(player_pos, treasure_pos):
    return player_pos == treasure_pos

# Taking input for the player positions
def get_move():
    
    move = input("Enter your move (up, down, left, right): ").lower()
   
    while move not in ['up', 'down', 'left', 'right']:
        print("Invalid move. Choose from: up, down, left, right.")
        move = input("Enter your move (up, down, left, right): ").lower()
    return move


def move_player(player_pos, move):   
    # tracking the input of the player on the
    if move == 'up' and player_pos[0] > 0:
        player_pos[0] -= 1
    elif move == 'down' and player_pos[0] < GRID_SIZE - 1:
        player_pos[0] += 1
    elif move == 'left' and player_pos[1] > 0:
        player_pos[1] -= 1
    elif move == 'right' and player_pos[1] < GRID_SIZE - 1:
        player_pos[1] += 1




# Function to start the game
def start_game():
    print("Welcome to the Treasure Hunt Game!")
    print(f"Your goal is to find the hidden treasure in a {GRID_SIZE}x{GRID_SIZE} grid.")
    print("You can move up, down, left, or right.")
    print("You have a limited number of moves to find the treasure.\n")

    # Randomly initialize player and treasure positions
    player_pos = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
    treasure_pos = [(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
    
# player_pos =[0,3]
# treasure_pos= [2,4]
    
   #TO  Ensure player and treasure do not start at the same position
    while player_pos == treasure_pos:
        treasure_pos = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
        
        
      

    moves_left = 10 # Set a limit on the number of moves
    print(player_pos)
    print(treasure_pos)
 

    while moves_left > 0:
        print(f"Moves left: {moves_left}")
        display_grid(player_pos)

        move = get_move()
        move_player(player_pos, move)

        
        if check_for_treasure(player_pos, treasure_pos):
            display_grid(player_pos)
            print("Congratulations!  you have found the treasure!")
            break

        moves_left -= 1

    if moves_left == 0 and not check_for_treasure(player_pos, treasure_pos):
        print("Sorry, you ran out of moves. Game over!")
        print(f"The treasure was at position {treasure_pos}.")


start_game()