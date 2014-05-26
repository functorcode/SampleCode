#author:Juned Munshi
#contact: juned@ymail.com

from sudoku import *
import sys
#visualization .set True to visualize all steps taken to solve puzzle
playback=True


#initialize puzzle from file
s=sudoku("puzzle.txt")
initState=s.initState;
print initState

#create gameboard
board=gameBoard("Brainy Agent solves Sudoku Problem",600,600,50,120)
#display sudoku puzzle
for key,value in initState.items():
	board.drawText(key[0],key[1],str(value))
board.draw()


print "Puzzle read successfully.Press Enter to solve puzzle"
sys.stdin.read(1)
#while (pygame.event.wait().type != KEYDOWN  ): pass

#note initial time
stime=time.time()

#record all the actions 
actions=[]

#solve sudoku
print "Please wait..."
solution= bts(initState,s,actions)


#visualize
if solution==False:
	print "No soultion found :(. Puzzle may be invalid"
else:
	print "Solved in ",time.time()-stime ," seconds"
	board.draw()
	counter=0
	if playback :
			for act in actions:
				counter=counter+1;
				if(act[0]=='a'):
					board.drawText(act[1][0][0],act[1][0][1],str(act[1][1]))
				else:
					board.removeText(act[1][0][0],act[1][0][1])
				board.draw()
	#print counter

	for i in range(9):
		line=""
		for j in range(9):
			line=line+str(solution[(i,j)])+" "
			board.drawText(i,j,str(solution[(i,j)]))
	
		print line,"\n"


#wait unitll user close the window
while(1):
	board.draw()
	if pygame.event.wait().type==pygame.QUIT:
		break; 
	