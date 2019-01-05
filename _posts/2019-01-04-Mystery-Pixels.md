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


## Solution 1

Inspection reveals a few interesting features of the pattern: 
- The zeroth row and column are all blue.
- Each row (and each column), apart from the zeroth, exhibits a repeating pattern: the pattern up to but not including the $x=y$ diagonal is followed by its inverse (the colors are switched), after which the original pattern and inverse are repeated, and so on (I confess that I did not take the trouble to check all of the rows and columns for this, but it seems to be true).  It follows that the diagonal itself, apart from $(0,0)$, is composed of $1$s.

It turns out that these two features uniquely determine the entire pattern.  Let's see how. We'll work in a spreadsheet where $(0,0)$ is at the top-left and where blue and red are replaced by $0$ and $1$.  Start by filling in the edges and diagonal.

![Edges and diagonal](/img/1.PNG)

Looking at column $1$, we see that its initial pattern, up to but not including the diagonal, is already complete: it is simply $0$. Its inverse is also already complete: it's the $1$ at $(1,1)$.  So we repeat the pattern $0,1$ through the rest of column $1$, and we do the same for row $1$:

![Row and column 1 complete](/img/2.PNG)

Now we see that the initial pattern for column $2$ is complete: it is $0,0$. So we continue with its inverse, namely $1,1$ and then repeat the pattern $0,0,1,1$ throughout the column.

![Row and column 2 complete](/img/3.PNG)

You get the idea: this can be repeated for every row and column, to determine the value of every pixel in the grid. When we've completed the $n$th row and column, we have all of the $n+1$st row and column up to the diagonal; so we know its base pattern, which we complete with its inverse and finish the row and column by repeating the base and inverse patterns.

![Grid complete](/img/4.PNG)

## Solution 2

Let's visualize the grid as part of a triangle, with the $(0,0)$ pixel at the top.  Letting blue now be represented as $1$ and red $0$ (for a reason that will emerge), we have:

```
                1
               1 1
              1 0 1
             1 1 1 1
            1 0 0 0 1
           1 1 0 0 1 1
          1 0 1 0 1 0 1
```

Now a different pattern emerges. Each number apart from the initial $1$ is the sum of the one or two numbers directly above it in the previous row, modulo $2$.  That means that this is a version of Pascal's Triangle, where the addition is modulo $2$ (this triangle has an interesting connection to Sierpinski's Triangle). This lets us connect the pattern to combinatorics and polynomial expressions: the value of the $i$th element of the $j$th row in the triangle is $j \choose i$ modulo $2$, or the coefficient of the $i$th power of $x$ in the expansion of $(x+y)^j$ modulo $2$.

<br>
