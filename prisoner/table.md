






| Payoff| P2  C | P2  D |
| ------|-------|------ |
| P1  C | -1,-1 | -3, 0 |
| P1  D |  0,-3 | -2,-2 |





### Many players tested 1 vs 1 (e.g. 14)
### Game played many rounds consecutively (e.g. 200)
### Final score per player is the sum of all scores

- **Player A**: Guaranteed to win each game**
- **Player B**: Guaranteed to tie or loose each game
- **Q2:** How condifent are you A will win* the tournament?
- **Q3:** How condifent are you B will win* the tournament?

???
- I promised talking about PD, but let's first look at a more generic example. This will hold true for PD and be useful in the future. Trust me ;D

I'll try to be neutral when asking the question. Just the prhasing already will influence the results, which words to choose? will win? will not win? will loose? confidence, sure, etc... good thing this is not a serious scientific study :D

*If players were to tie in final score, we consider both winners
**Played against an equivalent strategy will tie ^_^U

- Vote goes like this 5 means you are either in favour or against. 0 you think P will loose. 10 P will win. If confidence is too abstract think 6 a small amount of money, 7 modest amount, 8 a considerable amount, 9 a big amount, 10 a huge amount

- If people ask for clarifications: The number of rounds is finite and known in advance to each player (shouldn't matter yet).

---

# 1.2 Generalised

<div style="text-align:center"><img src="./briefcase_exchange.png" width="50%" /></div>
### Q4/Q5. You are the Buyer/Seller. What do you do?

???
Hofstadter suggests this transformation is easier to understand

---

# 1.3 PD Payoff matrix


| Actions| C           | D     |
| -------|------------:| -----:|
| C      | right-align | $1600 |
| D      | centered    |   $12 |
|        | are neat    |    $1 |





         player B
Actions| C    D
---------------------
A C    | -1,-1  -3, 0    C -> cooperate
A D    |  0,-3  -2,-2    D -> defect

- You can't comunicate
- You don't know the other
- You won't ever see each other again

Q5. You are player A. What do you do?

???
- explain nash equilibrium (dominant strategy)
- explain pareto efficiency
- explain superrational approach (not accepted by Game Theory as standard community)

---

# 1.4 PD Repeated game (finite, N iterations)

Reverse induction g1, g2, g3... gN-1, gN
- Determine move for gN.
  - Ignore previous iterations.

- Determine move for gN-1.
  - Game N is already fixed. Independent of prev.
  - Ignore previous iterations.

- We repeat this reasoning until we reach the g1

Q5. How condifent are you A will win* the tournament?
Q6. How condifent are you B will win* the tournament?

???
Explain why we can ignore previous iterations
This case is now for this specific game. Unlike previous question.
Player A: Guaranteed to win each game*
Player B: Guaranteed to tie or loose each game

---

# 1.5 Axelrod tournaments I
(200 iterations, 14 algorithms)
- Always cooperate
- JOSS
- Tit for Tat
- Always defect

---

# 1.6 Axelrod II and beyond
(unkown iterations, many more algorithms)
- Tit for 2 Tat (II)
- Tester (II)
- Pavlov (win-stay lose-shift (1992))
- Handshaking  # 20th

???
- It's you alone against the oponent, there is no randomness

----
