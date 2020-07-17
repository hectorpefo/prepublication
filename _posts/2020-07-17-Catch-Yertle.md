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

We'll change units every minute so that the distance remains $10$. What does change is that at minute $t$, each runner's pace is reduced by the multiplicative factor $\frac{t}{t+1}$. So between times $t$ and $t+1$, the tortoise's pace is:

$$v_t = \prod_{i=1}^t \frac{i}{i+1} = \frac{1}{t+1}$$

Letting $T_t$ be the position of the tortoise at the end of minute $t$ (just before the stretch), we have:

$$T_0 = 0$$

$$T_{t+1} = T_t + v_t$$

$$T_{t} = \sum_{i=1}^t \frac{1}{i}$$

Thus the tortoise's positions at integer minutes form the partial sums of the [harmonic series](https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)), which are also called harmonic numbers. Since the harmonic numbers grow approximately logarithmically, we know that the tortoise will get to $10$ miles eventually. 

This happens (very) shortly before the end of minute $12367$ (the $12367$th harmonic number is [the first to exceed $10$](https://oeis.org/A004080)). So we'll time the hare's departure to reach the line at that time. Relying on the fact that the hare's velocity is always $\frac{5}{4}$ times that of the tortoise, and allowing for starting between integer minutes (which is important because a great deal of speed is lost in the early minutes), we find computationally that the hare should start when $4$ minutes and $28.80$ seconds have elapsed. The race ends, tied, after about $8$ days, $14$ hours and $8$ minutes.

<br>