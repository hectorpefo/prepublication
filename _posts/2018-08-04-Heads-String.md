---
layout: post
date: 2018/08/04
title: Heads String
published: True
---

>I flip a coin. If it’s heads, I’ve won the game. If it’s tails, then I have to flip again, now needing to get two heads in a row to win. If, on my second toss, I get another tails instead of a heads, then I now need three heads in a row to win. If, instead, I get a heads on my second toss (having flipped a tails on the first toss) then I still need to get a second heads to have two heads in a row and win, but if my next toss is a tails (having thus tossed tails-heads-tails), I now need to flip three heads in a row to win, and so on. The more tails you’ve tossed, the more heads in a row you’ll need to win this game.
>
>I may flip a potentially infinite number of times, always needing to flip a series of N heads in a row to win, where N is T + 1 and T is the number of cumulative tails tossed. I win when I flip the required number of heads in a row.
>
>What are my chances of winning this game? (A computer program could calculate the probability to any degree of precision, but is there a more elegant mathematical expression for the probability of winning?)

<!--more-->

## Solution

You lose if you fail to throw a heads ($\frac{1}{2}$ chance of that), then fail to throw two heads in a row ($1-\frac{1}{4}$ chance of that), then fail to throw three heads in a row ($1-\frac{1}{8}$ chance of that), and so on. The chance of victory is one minus that of losing, and so it is:

$$1 - \prod_{i=1}^\infty \left(1-\frac{1}{2^i}\right) \approx .7112$$

<br>
