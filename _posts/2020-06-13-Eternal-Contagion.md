---
layout: post
published: true
title: Eternal Contagion
date: 2020-06-13
---

>You are studying a new strain of bacteria, Riddlerium classicum (or R. classicum, as the researchers call it). Each R. classicum bacterium will do one of two things: split into two copies of itself with probability $p$, or die. 
>
>If you start with a single R. classicum bacterium, what is the probability that it will lead to an everlasting colony?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/how-long-will-the-bacterial-colony-last/))

## Solution

Let $E_n$ be the event of there being extinction as of (or before) generation $n$. Then $P(E_0)$ is $0$, $P(E_1)$ is $(1-p)$, and since $E_{n+1}$ is equivalent to the disjunctive event of $E_1$ (going extinct immediately) and the negation of $E_1$ (having two offspring) followed by two instances of $E_{n}$:

$$P(E_{n+1}) = (1-p) + pP(E_{n})^2$$

Let's use $F(x)$ to abbreviate this function of $P(E_n)$. Then we have:

$$F(x) = (1-p) + px^2$$

So:

$$P(E_n) = F(F(\ldots F(0)\ldots)$$

where there are $n$ occurrences of $F$ (I will leave this unsaid henceforth). Where $E$ is the event of there eventually being extinction, we can see that $P(E)$ is a fixed point of $F$:

$$P(E) = lim_{n \rightarrow \infty} P(E_n) = 
lim_{n \rightarrow \infty} F(F(\ldots F(0)\ldots)
$$

As $n \rightarrow \infty$, $(F(n+1) - F(n)) \rightarrow 0$, and given the continuity of $F$:

$$F(P(E)) = F(lim_{n \rightarrow \infty}P(E_n)) 
= lim_{n \rightarrow \infty}F(P(E_n)) = P(E)$$

That gives us a quadratic equation in $P(E)$:

$$P(E) = (1-p) + pP(E)^2$$

For $p < .5$, this has two solutions, only one of which is in range: extinction with probability $1$.

For $p>.5$, there are also two solutions, namely $1$ and $\frac{1}{p} - 1$, which is less than $1$. Call the other solution, besides $P(E)$, whichever it may be, $q$. Now:

$$0 \leq q$$

Since $F$ is an increasing function, it follows that:

$$F(0) \leq F(q) = q$$

$$F(F(0)) \leq F(q) = q$$

$$\cdots$$

$$ F(F(\ldots F(0)\ldots) \leq q $$

$$ P(E) \leq q $$

Thus $P(E)$ cannot be the strictly greater solution (i.e., $1$) and hence must be $\frac{1}{p}-1$, and so the probability of eternal survival is $2 - \frac{1}{p}$.

<br>