---
layout: post
published: true
title: Extra Lives
date: 2018/06/15
---

>The live smartphone game show HQ Trivia has taken the world by storm. In the game, you face a sequence of 12 multiple-choice trivia questions, each with three choices. If you answer all 12 correctly, you win a cash prize!2 Get one question wrong, however, and you are eliminated. If you didn’t know much trivia but did know strategy, how many phones would you need to guarantee that you’d win the cash on one of them?
>
>Cool extra credit: The real-life game has an added wrinkle: extra lives, which you can earn by referring others to the game. You can use an extra life after you get a question wrong, and you continue just as if you had gotten that question right. However, you can use only one of these per game per phone. Assuming that all your phones have an extra life, how many phones do you need to guarantee a victory now?


<!--more-->

([fivethirtyeight](https://fivethirtyeight.com/features/how-many-phones-do-you-need-to-win-hq-trivia/))

## Solution

In $12$ questions there are $24$ incorrect answers. All answers must be covered to guarantee winning, and each incorrect answer costs a phone. Therefore, we need $24$ phones whose careers end with an incorrect answer. Plus we need one more, the phone whose career ends with the correct answer on the final question.  That makes $25$.

### Extra Credit

The best we can do is to use $13$ phones: at two incorrect answers per phone, the $24$ incorrect answers will kill off a maximum of $12$ of them, and so there will be at least one phone with lives remaining to give the correct final answer.

<br>
