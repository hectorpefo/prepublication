N = 4

def ExploreBoards(Queens):
	if len(Queens) == N:
		ExamineBoard(Queens)
		return
	if Queens == []:
		lastQueen = -1
	else:
		lastQueen = Queens[-1]
	for NewQueen in range(lastQueen+1,N**2-(N-len(Queens))+1):
		NewQueens = list(Queens)
		NewQueens.append(NewQueen)
		ExploreBoards(NewQueens)

def ExamineBoard(Queens):
	global Solutions
	for i in range(N-1):
		Queen = Queens[i]
		for j in range(i+1,N):
			Target = Queens[j]
			if Queen%N == Target%N:
				return
			if Queen/N == Target/N:
				return
			if ((Target-Queen)%(N-1)) == 0: 
				return
			if ((Target-Queen)%(N+1)) == 0: 
				return
	Solutions.append(Queens)

Solutions = []
ExploreBoards([])
print len(Solutions)
print Solutions
