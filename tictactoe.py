import numpy as np
from  time import sleep
import os

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def main():
	values = np.array([['','',''],['','',''],['','','']])
	freeSpace = 9;
	P1 = "X"
	P2 = "0"
	char = P1
	taken_cases = [0]*9 
	player1 = input("what's your name Player1 ? ")
	player2 = input("what's your name Player2 ? ")
	while freeSpace > 0 :
		clear_screen()
		printBoard(values)
		try : 
			
			char = P1 if freeSpace % 2 else P2
			cor = int(input(f"your choice {player1 if P1 == char else player2} : "))
			if cor in taken_cases:
				print("="*100)
				print("The case is Taken! , pick another one")
				print("="*100)
				sleep(2)
				continue

			if cor > 9 : 
				print("="*100)
				print("Number is too big !") 
				print("="*100)

				sleep(2)
				continue
			elif cor > 6 : 	
				values[2][cor-7] = char 
				taken_cases.append(cor)
			elif cor > 3 :
				values[1][cor-4] = char 
				taken_cases.append(cor)
			elif cor > 0 :
				values[0][cor-1] = char 
				taken_cases.append(cor)
			else:
				print("="*100)
				print("The number is too small !")
				print("="*100)
				sleep(2)
				continue
				
		except ValueError:
			print("="*100)
			print("Please pick a number between 1-9")
			print("="*100)
			sleep(2)
			continue

		if check_winner(values) == P1 or check_winner(values) == P2 :
				print(f"Winner is 🥳 {player1 if check_winner(values) == 'X' else player2} 🥳")
				print("🥳"*29) 
				return
		freeSpace-=1
	print("="*100)
	print()
	print("Draw.")
	print()
	print("="*100)
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


