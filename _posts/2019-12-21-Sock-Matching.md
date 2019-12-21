---
layout: post
published: true
title: Sock Matching
date: 2019/12/21
---

>I have $N$ pairs of socks in a drawer. I pull out socks (without replacement) until I have a matching pair. On average, how many socks does it take?
>
>Extra Credit: describe the behavior of this average for large $N$.

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/can-you-find-a-matching-pair-of-socks/))

## Solution

### A recurrent approach

Given $N$ pairs of socks, let $E_i$ be the expected number of (additional) socks you'll have to pull out to get a match, given that you have already pulled out $i$ non-matching socks. 

Then, $E_N$ is $1$, because when you have pulled out $N$ non-matching socks --- one from each pair --- you are certain to get a match on the next try.

Suppose you have pulled out $i$ socks, for $0 \leq i < N$. Then your probability of getting a match on the next try is $i/(2n-i)$. If you fail to get a match, you will then expect $E_{i+1}$ more tries. Therefore:

$$E_i = \frac{i}{2N-i} + \frac{2N-2i}{2N-i} \cdot (1 + E_{i+1})$$

This lets us calculate $E_i$ for any $i$, down to $E_0$, which is the overall expected number of pulled-out socks. In the case of $N=10$, it's about $5.68$ socks. 

### A combinatorial approach, and extra credit

With $N$ pairs of socks in the drawer, we will calculate the expected value $E(X)$ of the random variable $X$, the number of pulls to yield the first pair. We will rely on the fact that for a non-negative, integer-valued random variable:

$$E(X) = \sum_{i=0}^\infty P(X > i)$$

So let's find $P(X>i)$. There are ${2N \choose i}i!$ ways for the first $i$ pulls to go (choices of the socks multiplied by the number of their orderings), out of which some are ways in which no pair occurs. How many? There are ${N \choose i}$ choices of pairs to have already pulled a sock from, there are $2^i$ choices of particular socks from those pairs, and there are $i!$ orderings of those socks. So:

$$P(X>i) = \frac{ {N \choose i} 2^ii!}{ {2N \choose i} i!} = {2N \choose N}^{-1}{2N-i \choose N} 2^i $$

Because the greatest $i$ for which $P(X>i)$ is non-zero is $N$:

$$E(X) = {2N \choose N}^{-1}\sum_{i=0}^N {2N-i \choose N} 2^i$$

<br>
