from tictactoe import check_winner
import numpy as np




def test_check_winner():
	values =[]
	
	values.append([['X','0','0'],['X','0','0'],['X','0','0']])
	values.append([['0','X','X'],['0','X','X'],['0','X','X']])
	values.append([['0','',''],['0','',''],['X','','']])
	values.append([['','',''],['','',''],['','','']])
	assert check_winner(np.array(values[0])) == 'X'
	assert check_winner(np.array(values[1])) == '0'
	#assert check_winner(np.array(values[2])) == False 
	assert check_winner(np.array(values[3])) == False 
	

