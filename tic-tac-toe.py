import random

board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
  print('   0   1   2 \n')
  for row in range(3):
    print(f'{row}  ' + ' | '.join(board[row]))
    if row < 2:
      print('  ---+---+---')



def make_human_move(board, player):
  while True:
   try:
      row = int(input("Enter number for row(0 - 2): "))
      col = int(input("Enter number for col(0 - 2): "))
      if 0 <= row <= 2 and 0 <= col <= 2:
         if board[row][col] == ' ':
            board[row][col] = player
            break
         else:
            print("Spot taken! Try again")
      else:
         print('Enter number between (0 - 2)')
   except ValueError:
     print("Enter Valid Numbers")

def make_computer_move(board, player):
  while True:
   row = random.randint(0, 2)
   col = random.randint(0, 2)
   if board[row][col] == ' ':
      board[row][col] = player
      break

def check_winner(board, player):
  for row in board:
    if all(cell == player for cell in row):
      return True
   
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True
    
  if all(board[i][i] == player for i in range(3)):
    return True
  if all(board[i][2-i] == player for i in range(3)):
    return True
  
  return False

def play_game():
   print("Start Game")
   print('Initial Board')
   print_board(board)
   print("\n")
   for i in range(9):
      human = 'X'
      computer = 'O'
      player = human if i%2==0 else computer
      print(f"Turn {i+1}: Player {player}")

      if player == human:
         make_human_move(board, player)
      else:
         make_computer_move(board, player)
         print("Computer thinking....")

      print_board(board)
      print("\n")

      if check_winner(board, player):
         print(f"Player {player} won!")
         if player == human:
            print("You won!")
         else:
            print("Computer won!")
         break
      
   else:
      print("It is a draw!")

while True:
  print("===NEW GAME=== \n")
  play_game()

  replay = input("Do you want to play again(click 'r')?: ")
  if replay.lower().strip() != 'r':
    break

