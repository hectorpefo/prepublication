DEPTH = 43

total = 1.0/2
for n in range(1,DEPTH+1):
	product = 1
	for i in range(1,n+1):
		product *= 2**i - 1
	total += 1.0*product/2**((n+1)*(n+2)/2.0)
	print(n,total)

from random import randint

REPS = 100000
MAX_FLIPS = 1000

accum = 0
for _ in range(REPS):
	tails = 0
	headsStreak = 0
	flips = 0
	while True:
		flip = randint(0,1)
		if flip == 0:
			tails += 1
			headsStreak = 0
		else:
			headsStreak += 1
			if headsStreak > tails:
				accum += 1
				break
		flips += 1
		if flips == MAX_FLIPS:
			break

print(accum*1.0/REPS)



