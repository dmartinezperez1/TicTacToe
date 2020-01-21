
#--------Global Variables-----

#game board
board = ["-","-","-",
		"-","-","-",
		"-","-","-"]
game_still_going=True
#Who Won? 
winner = None
#Whos turn is it?
current_player = "X"
#input range
input_range = ["1","2","3",
		"4","5","6",
		"7","8","9"]

#-------.code-------

def display_board():
	print(board[0]+ " | " + board[1] + " | " + board[2])
	print(board[3]+ " | " + board[4] + " | " + board[5])
	print(board[6]+ " | " + board[7] + " | " + board[8])

def play_game():
  #Display Board
  display_board()
  #While the game is still going
  while game_still_going:
    handle_turn(current_player)
    #Check if the game is over
    check_if_over()
    #Function to flip player
    flip_player()
  #Check who won and print out 
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")

def handle_turn(current_player):
  #Print who's turn 
  print(current_player + "'s turn.")
  #prompt user to input
  position = input("Pick a position from 1-9: ")

  valid = False
  while not valid:

    #If user inputs invalid input prompt again
    while position not in input_range:
      position = input("Invalid. Pick a position from 1-9: ")
    
    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("Space taken")

  board[position] = current_player
  display_board()

def check_if_over():
  #Call two separte functions to check if won or tie
	check_if_win()
	check_if_tie()

def check_if_win():
  #Set up global variables
  global winner

  #check rows
  row_winner=check_rows()
  #check columns
  column_winner=check_columns()
  #check diagonals
  diagonal_winner=check_diagonals()
  
  if row_winner:
    #there is a winner
    winner=row_winner
  elif column_winner:
    #there is a winner
    winner=column_winner
  elif diagonal_winner:
    #there is a winner
    winner=diagonal_winner
  else:
    #there is no win
    winner=None
  return

def check_if_tie():
  #set gloabl variables
  global game_still_going

  #If there is no dash AND no winner, then TIE
  if "-" not in board:
    game_still_going = False
  return

def check_rows():
  #set global Variables
  global game_still_going

  #Check to see if any rows are equal to each other but not equal to "-"
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6 ]== board[7] == board[8] != "-"
  #if any row is winner, end game
  if row_1 or row_2 or row_3:
    game_still_going=False

  #Find id X or O won
  if row_1:
    return board[0]
  if row_2:
    return board[3]
  if row_3:
    return board[7]
  return

def check_columns():
  #set up global variables
  global game_still_going

  #Check if the 3 columns are equal to each other but not "-"
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  #End game if any of the 3 rows match 
  if column_1 or column_2 or column_3:
    game_still_going=False
  
  #Find the winning player 
  if column_1:
    return board[0]
  if column_2:
    return board[1]
  if column_3:
    return board[2]
  
  return

def check_diagonals():
  #set up global variables 
  global game_still_going

  #check the two diagonals
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"

  #End game if there is a winner
  if diagonal_1 or diagonal_2:
    game_still_going = False
  
  #Find winning player
  if diagonal_1:
    return board[0]
  if diagonal_2:
    return board[8]
  return

def flip_player():
  global current_player
	#Alternate between players
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player ="X"
  return

play_game()
