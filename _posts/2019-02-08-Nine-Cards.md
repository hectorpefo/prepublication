---
layout: post
published: true
title: Nine Cards
date: 2019/02/08
---

>You and I are playing a game. It’s a simple one: Spread out on a table in front of us, face up, are nine index cards with the numbers 1 through 9 on them. We take turns picking up cards and putting them in our hands. There is no discarding.
>
>The game ends in one of two ways. If we run out of cards to pick up, the game is a draw. But if one player has a set of three cards in his or her hand that add up to exactly 15 before we run out of cards, that player wins. (For example, if you had 2, 4, 6 and 7, you would win with the 2, 6 and 7. However, if you had 1, 2, 3, 7 and 8, you haven’t won because no set of three cards adds up to 15.)
>
>Let’s say you go first. With perfect play, who wins and why?
<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/525600-minutes-of-math/))


## Solution

The 8 triples that sum to 15 are:
```
9,5,1 8,6,1 7,6,2 6,5,4
9,4,2 8,5,2 7,5,3
      8,4,3
```

A losing player making their last move must face a predicament wherein their opponent has two ways to sum to 15 with two of the remaining cards, for if there's only one way, they can just pick up whichever card the opponent needs.  Now, this can never happen with the opponent (who would have to be the first player after their fourth turn) holding cards A, B, C, D such that two pairs of them sum to 15 each with one remaining card.  For then a win would have been available to them on the fourth turn.  So it must be a situation where cards A, B, and C sum to 15 with still-available cards D and E as follows: A+C+D and B+C+E.  In that case, neither A nor B can have been chosen on the last turn, because then there would again have been a win available instead; so it can only have been C, the common card in the sums.  

We find the optimal game by recursively calling a function that yields the
optimally-played completion of a given partially-played game.  It turns out
that the best either player can do is to draw.  The particular draw that this
code lands on doesn't really matter, but the hands are 
`[[9, 8, 3, 6, 2], [5, 7, 4, 1]]`.  

```python

# Nine-card game played optimally.  Players are 0 and 1, cards are 1 to 9.

def handWins(hand):
	if len(hand) < 3:
		return False
	for i in range(len(hand) - 2):
		for j in range(i+1, len(hand) - 1):
			for k in range(j+1,len(hand)):
				if hand[i] + hand[j] + hand[k] == 15:
					return True
	return False

def getOptimalCompletion(hands, nextPlayer):
	# if game's over, return the result and the hands
	if handWins(hands[0]):
		return [0,hands]
	elif handWins(hands[1]):
		return [1,hands]
	elif len(hands[0]) == 5:
		return [2,hands]
	# otherwise, find the best optimal completion available by playing each
	# of the remaining cards, and return that.
	bestOptimalCompletion = []
	for nextCard in range(1,10):
		if nextCard in hands[0] or nextCard in hands[1]:
			continue
		newHands = [list(hands[0]), list(hands[1])]
		newHands[nextPlayer].append(nextCard)
		OptimalCompletion = getOptimalCompletion(newHands, 1 - nextPlayer)
		result = OptimalCompletion[0]
		if result == nextPlayer:
			return OptimalCompletion
		elif result == 2 or bestOptimalCompletion == []:
			# a draw or a loss but the first card tested
			bestOptimalCompletion = OptimalCompletion
	return bestOptimalCompletion

print(getOptimalCompletion ([[],[]],0))

```

<br>
