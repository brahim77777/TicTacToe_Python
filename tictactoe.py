import numpy as np
import os

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def main():
	values = np.array([['','',''],['','',''],['','','']])
	freeSpace = 9;
	P1 = "X"
	P2 = "0"
	char = P1
	player1 = input("what's your name Player1 ? ")
	player2 = input("what's your name Player2 ? ")
	while freeSpace > 0 :
		clear_screen()
		printBoard(values)
		try : 
			
			char = P1 if freeSpace % 2 else P2
			cor = int(input(f"your choice {player1 if P1 == char else player2} : "))
			if cor > 9 : 
				print("invalid choice!") 
				continue
			elif cor > 6 : 	
				values[2][cor-7] = char 
			elif cor > 3 :
				values[1][cor-4] = char 
			elif cor > 0 :
				values[0][cor-1] = char 
			else:
				print("="*100)
				print("the number Not COrrecct!")
				print("="*100)
				continue
				
		except ValueError:
			print("="*100)
			print("Error")
			print("="*100)
			continue

		if check_winner(values) == P1 or check_winner(values) == P2 :
				print(f"Winner is 🥳 {player1 if check_winner(values) == 'X' else player2} 🥳")
				print("🥳"*29) 
				return
		freeSpace-=1
# ------------------ : first border
# | --- |  O  |  X  |
# | --- | --- | --- |
# | --- | --- | --- |
# ------------------ : last border
#

def printBoard(values):
	print("-"*21)
	count = 1
	for i  in range(3):
		for j in range(3):
			if values[i][j] : 
				print(f"|  {values[i][j].upper()}  |", end="")
			else : 	
				print(f"| ({count}) |",end="")
			count +=1
		print()
		print("-"*21)

def check_winner(values ):
	for i in range(3):
		if check_triple(values[i]):
			return  check_triple(values[i]) 
	for i in range(3):
		if check_triple(values.T[i]):
			return check_triple(values.T[i])

	if check_triple(np.diag(values)):
		return check_triple(np.diag(values))

	if check_triple(np.diag(values[::-1]	))	:
		return check_triple(np.diag(values[::-1]))
	
def check_triple( triple ):
	if triple[0] == triple[1] == triple[2]:
		return triple[0]
	else:
		return False
	


if __name__ == "__main__" :
	main()


