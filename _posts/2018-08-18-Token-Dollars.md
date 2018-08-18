---
layout: post
published: true
title: Token Dollars
date: 2018/08/18
---

>Ariel, Beatrice and Cassandra — three brilliant game theorists — were bored at a game theory conference (shocking, we know) and devised the following game to pass the time. They drew a number line and placed $1 on the 1, $2 on the 2, $3 on the 3 and so on to $10 on the 10.
>
>Each player has a personalized token. They take turns — Ariel first, Beatrice second and Cassandra third — placing their tokens on one of the money stacks (only one token is allowed per space). Once the tokens are all placed, each player gets to take every stack that her token is on or is closest to. If a stack is midway between two tokens, the players split that cash.
>
>How will this game play out? How much is it worth to go first?
>
>A grab bag of extra credits: What if the game were played not on a number line but on a clock, with values of $1 to $12? What if Desdemona, Eleanor and so on joined the original game? What if the tokens could be placed anywhere on the number line, not just the stacks?
<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/step-1-game-theory-step-2-step-3-profit/)))

## Solution

With three players, there are only 10 times 9 times 8, or 720 courses for a game to run.  For each of the 90 ways for Ariel and Beatrice to chose numbers, we can find the best move for Cassandra, and discard the other 630 courses as irrelevant.  Then for each of the 10 numbers Ariel might choose, we can find which of the 9 numbers Beatrice might choose gives her the best result among the remaining course in which Cassandra chooses optimally; we discard the remaing 80 games. Finally we evaluate Ariel's outcome in the remaining 10 courses, in which both Beatrice and Cassandra choose optimally, and we select the one in which she does best.

The code below does this using recursion.  A game state is a sequence of moves (chosen numbers), starting with the empty sequence `[]`.  The function `getBestMove(state)` returns the optimal next move for the given game state.  That is found by trying out each of the next player's available moves and evaluating how that player fares if the game proceeds afterwards with optimal moves, which are found with the `getBestMove` function itself, called now on states that include one added move (there's the recursion).

Using this code, we find that for 3, 4, 5, 6, and 7 players, the optimal first moves are 5, 7, 4, 4, and 10, and the payoffs for the first player are 21, 17, 12.5, 12.5 and 10, respectively. The optimally-played game of 3 players is 5, 9, 8. For 3 players playing on a clock, the optimal first move is 7, with a payoff of 31.5.

For the continous case, we'll see that Ariel and Beatrice continue to profit from occupying numbers 5 and 9, while now Cassandra is indifferent between any location greater than 7 and less than or equal to 8 (because for any such choice, she will claim stacks 7 and 8).  

Suppose first that Ariel goes below 5.  Then Beatrice can either choose 9 (to get the 19 payoff), leaving 8, 7, and 6 for Cassandra to pick up (totalling 21) with any chosen number just over 7, or Beatrice can choose a number greater than 8 and less than 9, opening up the 19 payoff to Cassandra while netting only 15 herself, or she can go below 8, opening up 8, 9, and 10 for Cassandra's payoff of 27 while she gets only 13.  So Beatrice will in fact choose 9, Cassandra will secure 6, 7, and 8, leaving Ariel with a payoff of only 15.

Suppose now that Ariel chooses a number greater than 5. If it's greater than 5 but less than or equal to 6, Beatrice will choose 9 and Cassandra will choose any number closer to 5 than Ariels, for a payoff of 15, leaving Ariel with 13. If it's greater than 6, but less than or equal to 7, Beatrice will choose a number greater than or equal to 8, securing a payoff of 27, while Cassandra chooses any number nearer 6 than Ariels, for a payoff of 21, while Ariel gets 13. If greater than 7 but less than 8, Beatrice chooses any number less than or equal to 7 but closer than Ariel's, getting a payoff of 28 while Cassandra ends up with 8, 9, and 10, and Ariel gets nothing.  If it's  

<br>
