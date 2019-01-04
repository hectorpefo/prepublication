---
layout: post
published: true
title: Mystery Pixels
date: 2019/01/04
---

>What are these bits?

<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/what-the-heck-are-these-dang-bits/))

![Pixelized square image.](/img/ellenberg.png)


## Solution

Coming as it does from math professer Jordan Ellenberg, this puzzle may well have a slicker solution/explanation than this, but here's what I have.

Inspection reveals a few interesting features of the pattern: 
- The zeroth row and column are all blue.
- Apart from $(0,0)$, the pixels on the $x=y$ diagonal are all red.
- Each row (and each column) exhibits a repeating pattern: the pattern up to but not including the diagonal is followed by its inverse (the colors are switched), after which the original pattern and inverse are repeated, and so on.

It turns out that these features uniquely determine the entire pattern.  Let's see how. We'll work in a spreadsheet where $(0,0)$ is at the top-left and where blue and red are replaced by $0$ and $1$.  Start by filling in the edges and diagonal:

![Edges and diagonal](/img/1.PNG)

Looking at column $1$, we see that it's initial pattern, up to but not including the diagonal, is already complete: it is simply $0$. Its inverse is also already complete: it's the $1$ at $(1,1)$.  So we repeat the pattern $0,1$ through the rest of column $1$, and we do the same for row $1$:

![Row and column 1 complete](/img/2.PNG)

Now we see that the initial pattern for column $2$ is complete: it is $0,0$. So we continue with its inverse, namely $1,1$ and then repeat the pattern $0,0,1,1$ throughout the column.

![Row and column 2 complete](/img/3.PNG)

You get the idea: this can be repeated for every row and column, to determine the value of every pixel in the grid.

![Grid complete](/img/4.PNG)

<br>
