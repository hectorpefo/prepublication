---
layout: post
published: true
title: Catch Yertle
date: 2020-07-17
---

>The tortoise and the hare are about to begin a 10-mile race along a “stretch” of road. The tortoise is driving a car that travels 60 miles per hour, while the hare is driving a car that travels 75 miles per hour. (For the purposes of this problem, assume that both cars accelerate from 0 miles per hour to their cruising speed instantaneously.)
>
>The hare does a quick mental calculation and realizes if it waits until two minutes have passed, they’ll cross the finish line at the exact same moment. And so, when the race begins, the tortoise drives off while the hare patiently waits.
>
>But one minute into the race, after the tortoise has driven 1 mile, something extraordinary happens. The road turns out to be magical and instantaneously stretches by 10 miles! As a result of this stretching, the tortoise is now 2 miles ahead of the hare, who remains at the starting line.
>
>At the end of every subsequent minute, the road stretches by 10 miles. With this in mind, the hare does some more mental math.
>
>How long after the race has begun should the hare wait so that both the tortoise and the hare will cross the finish line at the same exact moment?

[(fivethirtyeight)](https://fivethirtyeight.com/features/can-the-hare-beat-the-tortoise/)

<!--more-->

## Solution

The key effect of the growing road is that it decreases the runners' velocities relative to the road's length. So we can equivalently consider a constant-length, ten-mile road with periodically diminishing velocities: at (integer) minute $t$, each runner's pace is reduced by the multiplicative factor $\frac{t}{t+1}$. So between times $t$ and $t+1$, the tortoise's pace in miles per minute is:

$$v_t = \prod_{i=1}^t \frac{i}{i+1} = \frac{1}{t+1}$$

Letting $T_t$ be the position of the tortoise at the end of minute $t$, we have:

$$T_0 = 0$$

$$T_{t+1} = T_t + v_t$$

$$T_{t} = \sum_{i=1}^t \frac{1}{i}$$

Thus the tortoise's positions at integer minutes form the partial sums of the [harmonic series](https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)), which are also called harmonic numbers. Since the harmonic numbers grow approximately logarithmically, we know that the tortoise will get to $10$ miles eventually. 

This happens during minute $12367$ (the $12367$th harmonic number is [the first to exceed $10$](https://oeis.org/A004080)). Going computational (see below), we find that the tortoise finishes more precisely on day $8$, after $14$ hours, $6$ minutes, and about $28.09$ seconds. So we'll time the hare's departure to reach the line at that time as well. We find that the hare should start when $3$ minutes and $35$ seconds have elapsed.

Code (Python):

```python
# Tortoise runs at a pace of 1/minute (mi/min), where minute
# is the next integer minute.

minute = 0
distance = 0
while distance < 10:
	minute += 1
	distance += 1/minute
# adjust for overshooting 10mi
tortoise_finish_time = minute - (distance - 10) / (1/minute)

# Hare runs at 1.25/minute similarly. We loop over start times 
# (h0) until the finish time matches Tortoise's. We identify
# the ballpark with a coarse h0Delta, and then manually refine 
# as we start with an h0 near the actual value, as here:

h0Delta = 1/100000000
h0 = 3.58333
while True:
	if h0 != int(h0):
		# progress to next integer minute
		distance = (1/(int(h0) + 1)) * (1 - (h0 - int(h0)))
		minute = int(h0) + 1
	else:
		distance = 0
		minute = h0
	while distance < 10:
		minute += 1
		distance += 1.25/minute
	# same correction for overshooting
	hare_finish_time = minute - (distance - 10) / (1.25/minute)
	if hare_finish_time >= tortoise_finish_time:
		hare_start_time = h0
		break
	h0 += h0Delta

from datetime import timedelta
print("Tortoise finishes in",
	str(timedelta(minutes=tortoise_finish_time)))
print("Hare starts at",
	str(timedelta(minutes=hare_start_time)),
	" and finishes in", 
	str(timedelta(minutes=hare_finish_time)))
```
 Output:

 ```
 Tortoise finishes in 8 days, 14:06:28.086999
Hare starts at 0:03:35  and finishes in 8 days, 14:06:28.087989
[Finished in 0.3s]
```

<br>