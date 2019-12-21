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


<br>
