N = 8

def ExploreBoards(Queens,Remaining):
	global Solutions, N
	if len(Queens) == N:
		Solutions.append(Queens)
		return
	# Add a new queen from Remaining. Since queens are added in numerical order,
	# ensure there are enough remaining to reach N queens.
	for i in range(len(Remaining)-(N-len(Queens))+1):
		# Copy the list so that the original is still around as we loop
		NewQueens = list(Queens)
		NewQueens.append(Remaining[i])
		# Since queens are added in order, remove earlier remaining candidates.
		NewRemaining = Remaining[i+1:len(Remaining)]
		pruneRemaining(NewQueens,NewRemaining)
		if len(NewRemaining) < N - len(NewQueens):
			# Not enough candidates remaining to reach N queens
			return
		ExploreBoards(NewQueens,NewRemaining)

def pruneRemaining(Queens,Remaining):
	# Remove candidates that the last-added queen can attack.
	global N
	Queen = Queens[-1]
	toRemove = []
	for Target in Remaining:
		ok = True
		if Queen%N == Target%N:
			# same rank
			ok = False
		elif Queen//N == Target//N:
			# same file
			ok = False
		elif onDiagonal(Queen,Target):
			ok = False
		if not ok:
			toRemove.append(Target)
	for Target in toRemove:
		Remaining.remove(Target)

def onDiagonal(Queen,Target):
	global N
	itsOn = 0
	if Target < Queen:
		if Target%N < Queen%N:
			# Target to lower left of Queen
			if (Queen-Target)%(N+1) == 0:
				itsOn = 1
		else:
			# Target below or to lower right
			if (Queen-Target)%(N-1) == 0:
				itsOn = 1
	else:
		if Target%N < Queen%N:
			# Target to upper left
			if (Target-Queen)%(N-1) == 0:
				itsOn = 1
		else:
			# Target above or to upper right
			if (Target-Queen)%(N+1) == 0:
				itsOn = 1
	return itsOn

def printBoard(Queens):
	for row in range(N-1,-1,-1):
		rowString = ""
		for col in range(N):
			if N*row+col in Queens:
				rowString += "Q"
			else:
				rowString += "*"
			rowString += " "
		print rowString

Solutions = []
All = list(range(N**2))
ExploreBoards([],All)
print "There are ",len(Solutions),"solutions for N =",N
print "The first is:"
printBoard(Solutions[0])