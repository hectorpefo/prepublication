from math import log,sqrt,pi,acos

STEPS = 10000000
TARGET_DIFF = .0001

def arcLength(theta,a,b):
	return .5*a*(theta*sqrt(1+theta**2) + log(theta + sqrt(1+theta**2)))

a = 1.0/pi
totalArcLength = arcLength(pi,a)
for step in range(1,STEPS+1):
	t = step*1.0/STEPS
	d2ByArcLength = totalArcLength - arcLength(acos(t),a)
	v = sqrt(1-t**2)/t
	d2ByTime = v*(1-t)
	if abs(d2ByArcLength - d2ByTime) < TARGET_DIFF:
		print (v,t)
	#print (v,t,d2ByArcLength,d2ByTime)

print(arcLength(pi,a), arcLength(0,a))

