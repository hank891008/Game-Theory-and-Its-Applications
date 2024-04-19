# **Assignment I: Fictitious Play**

**[535608] Game Theory and Its Applications by Prof. Li-Hsing Yen**
 <font color="#f00">Deadline: 2023/10/23 23:59</font>

---

## 1. Overview 

 a. Implement the framework of the game matrice
 b. Implement the fictitious play to solve the game
 c. Write a report to answer the questions and summarize your analysis

---

## 2. Introduction to fictious play

Fictitious play is one of the earliest learning rules defined by George W. Brown [1] who conjectured its convergence to the value of a zero-sum game. Its convergence properties were established by Julia Robinson [2]. It was actually not proposed initially as a learning model at all, but rather as an iterative method for computing **Nash equilibria** in zero-sum games[3,4]. It happens to not be a particularly effective way of performing this computation, but since it employs an intuitive update rule, it is usually viewed as a model of learning. 

> :mag_right: Nash equilibrium: a strategy profile (game state) where no player can further increase its own utility by unilaterally changing its strategy.

Fictitious play is an instance of model-based learning, in which the learner explicitly maintains beliefs about the opponent’s strategy. The structure of such techniques is straightforward.
```
Initialize beliefs about the opponent’s strategy
repeat
| Play a best response to the assessed strategy of the opponent
|_Observe the opponent’s actual play and update beliefs accordingly
```
> :pencil: Note: In this scheme, the agent is oblivious to the payoffs obtained by other agents. We assume that each agent only knows his own payoff matrix in the stage game.

In fictitious play, an agent believes that his opponent is playing the mixed strategy given by the empirical distribution of the opponent’s previous actions. That is, if $A$ is the set of the opponent’s actions, and for every $a ∈ A$ we let $w(a)$ be the number of times that the opponent has played action $a$, then the agent assesses the probability of $a$ in the opponent’s mixed strategy as

$$P(a) = \frac{ w(a) }{ \sum_{a'∈ A}{w(a')} }.$$

For example, in a repeated **Prisoner’s Dilemma** game.
|                        | stays silent ($S$) | betrays ($B$) |
|:----------------------:|:------------------:|:-------------:|
| **stays silent ($S$)** |      (-1,-1)       |    (-3,0)     |
|   **betrays ($B$)**    |       (0,-3)       |    (-2,-2)    |

If Player 1 has played $S, S, B, S, B$ in the first five games, which means that Player 2 begins the game with the prior belief (3,2) before the sixth game. On the other hand, if Player 2 has played $S, B, S, S, B$ in the first five games, which means that Player 1 begins the game with the prior belief (3,2). How will the players play in the fictitious play process?

| Round | 1's action | 2's action | 1's belief | 2's belief | 1's payoff  | 2's payoff  |
|:-----:|:----------:|:----------:|:----------:|:----------:|:-----------:|:-----------:|
|   0   |     -      |     -      |   (3,2)    |   (3,2)    |  -9 ++-4++  |  -9 ++-4++  |
|   1   |    $B$     |    $B$     |   (3,3)    |   (3,3)    | -12 ++-6++  | -12 ++-6++  |
|   2   |    $B$     |    $B$     |   (3,4)    |   (3,4)    | -15 ++-8++  | -15 ++-8++  |
|   3   |    $B$     |    $B$     |   (3,5)    |   (3,5)    | -18 ++-10++ | -18 ++-10++ |
|  ...  |    ...     |    ...     |    ...     |    ...     |     ...     |     ...     |

Observe that it can converge to pure-strategy NE Nash equilibrium, i.e., ($B$,$B$ ) in Prisoner’s Dilemma game by fictitious play. Another example, in a repeated **Matching Pennies** game.

|                 | Heads ($H$) | Tails ($T$) |
|:---------------:|:-----------:|:-----------:|
| **Heads ($H$)** |   (1,-1)    |   (-1,1)    |
| **Tails ($T$)** |   (-1,1)    |   (1,-1)    |

Assume that Player 1 begins the game with the prior belief that Player 2 has played $H$ 1.5 times and $T$ 2 times. Player 2 begins with the prior belief that Player 1 has played $H$ 2 times and $T$ 1.5 times. How will the players play in the fictitious play process?

| Round | 1's action | 2's action | 1's belief | 2's belief |  1's payoff  |  2's payoff   |
|:-----:|:----------:|:----------:|:----------:|:----------:|:------------:|:-------------:|
|   0   |     -      |     -      |  (1.5,2)   |  (2,1.5)   | -0.5 ++0.5++ | -0.5 ++0.5++ |
|   1   |    $T$     |    $T$     |  (1.5,3)   |  (2,2.5)   | -1.5 ++1.5++ | ++0.5++ -0.5  |
|   2   |    $T$     |    $H$     |  (2.5,3)   |  (2,3.5)   | -0.5 ++0.5++ | ++1.5++ -1.5  |
|   3   |    $T$     |    $H$     |  (3.5,3)   |  (2,4.5)   | ++0.5++ -0.5 | ++2.5++ -2.5  |
|   4   |    $H$     |    $H$     |  (4.5,3)   |  (3,4.5)   | ++1.5++ -1.5 | ++1.5++ -1.5  |
|   5   |    $H$     |    $H$     |  (5.5,3)   |  (4,4.5)   | ++2.5++ -2.5 | ++0.5++ -0.5  |
|   6   |    $H$     |    $H$     |  (6.5,3)   |  (5,4.5)   | ++3.5++ -3.5 | -0.5 ++0.5++  |
|   7   |    $H$     |    $T$     |  (6.5,4)   |  (6,4.5)   | ++2.5++ -2.5 | -1.5 ++1.5++  |
|  ...  |    ...     |    ...     |    ...     |    ...     |     ...      |      ...      |

> :pencil: Note: If a player has at least two best responses related to expected payoff in each round, then he will pick one action randomly from the best response set .

As you can see, each player ends up alternating back and forth between playing $H$ and $T$. In fact, as the number of rounds tends to infinity, the empirical distribution of the play of each player will converge to (0.5,0.5), which is the same as the mixed strategy Nash equilibrium.

---
## 3. Questions and Requirements

Fictitious play has several nice properties[5-7] although it is actually not proposed initially as a learning model at all. In this section, we'll ask you to implement it in programming language whatever you like and answer the following questions in your report.

#### Q1.(10%) One pure-strategy Nash Equilibrium
See the following game matrix
|           |  $c_1$  | $c_2$ |
|:---------:|:-------:|:-----:|
| **$r_1$** | (-1,-1) | (1,0) |
| **$r_2$** |  (0,1)  | (3,3) |

It has only one pure-strategy Nash equilibrium $(r_2,c_2)$. Can it converge to the pure-strategy Nash equilibrium by fictitious play? Please justify your answer clearly.

#### Q2.(10%) Two or more pure-strategy NE
See the following game matrix
|           | $c_1$ | $c_2$ |
|:---------:|:-----:|:-----:|
| **$r_1$** | (2,2) | (1,0) |
| **$r_2$** | (0,1) | (3,3) |

It has two pure-strategy Nash equilibria $(r_1,c_1)$, $(r_2,c_2)$ respectively. Can it converge to the both of the pure-strategy Nash equilibria by fictitious play? Or just one of them? Please justify your answer.

#### Q3.(10%) Two or more pure-strategy NE (Conti.)
See the following game matrix
|           | $c_1$ | $c_2$ |
|:---------:|:-----:|:-----:|
| **$r_1$** | (1,1) | (0,0) |
| **$r_2$** | (0,0) | (0,0) |

It also has two pure-strategy Nash equilibria $(r_1,c_1)$, $(r_2,c_2)$ respectively. Can it converge to the both of the pure-strategy Nash equilibria by fictitious play? Or just one of them? Please justify your answer.

#### Q4.(10%) Mixed-Strategy Nash Equilibrium
See the following game matrix
|           | $c_1$ | $c_2$ |
|:---------:|:-----:|:-----:|
| **$r_1$** | (0,1) | (2,0) |
| **$r_2$** | (2,0) | (0,4) |

Although it has no pure-strategy Nash equilibrium, there exists a mixed-strategy Nash equilibrium, i.e., $P(r_1)=\frac{4}{5}$, $P(r_2)=\frac{1}{5}$ for Player 1 and $P(c_1)=\frac{1}{2}$, $P(c_2)=\frac{1}{2}$ for Player 2. Can it converge to the mixed-strategy Nash equilibrium by fictitious play? Please justify your answer.

#### Q5.(10%) Best-reply path
See the following game matrix
|           | $c_1$ | $c_2$ |
|:---------:|:-----:|:-----:|
| **$r_1$** | (0,1) | (1,0) |
| **$r_2$** | (1,0) | (0,1) |

Although it has no pure-strategy Nash equilibrium, there exists a finite best-reply path. Can it converge to the mixed-strategy Nash equilibrium by fictitious play? Please justify your answer.

:::info
:bulb: **Hint:** From *Q6* to *Q10*, please initialize beliefs about the opponent’s strategy in different way. Or you may ignore some possible solutions and cannot get the whole score in each question. Actually, you can just randomly assign the value and observe the result.
:::

#### Q6.(10%) Pure-Coordination Game
There are two main characteristics for the pure-coordination game. One is that both players prefer the same Nash equilibrium outcome. The other is that both of them have identical interest[8]. See the following game matrix
|           |  $c_1$  |  $c_2$  |
|:---------:|:-------:|:-------:|
| **$r_1$** | (10,10) |  (0,0)  |
| **$r_2$** |  (0,0)  | (10,10) |

There exists two pure-strategy Nash equilibria, including $(r_1,c_1)$ and $(r_2,c_2)$. In addition, it also has a mixed-strategy Nash equilibrium, i.e., $P(r_1)=\frac{1}{2}$, $P(r_2)=\frac{1}{2}$ and $P(c_1)=\frac{1}{2}$, $P(c_2)=\frac{1}{2}$. Can it converge to the pure-strategy Nash equilibria by fictitious play? Or converge to mixed-strategy Nash equilibrium? Please justify your answer.

#### Q7.(10%) Anti-Coordination game
Compared to pure coordination game, it can be thought of as the opposite of a coordination game. In pure-coordination game, sharing the resource creates a benefit for all. In contrast, the resource is rivalrous but non-excludable in anti-coordination games and sharing comes at a cost. See the following game matrix
|           | $c_1$ | $c_2$ |
|:---------:|:-----:|:-----:|
| **$r_1$** | (0,0) | (1,1) |
| **$r_2$** | (1,1) | (0,0) |

There exists three Nash equilibria as well, including two pure-strategy Nash equilibria and one mixed-strategy Nash equilibrium. The pure-strategy equilibria are in the upper right corner $(r_1,c_2)$ and the lower left corner $(r_2,c_1)$ respectively. And the mix-strategy Nash equilibrium can be simply obtained by partial derivative, which is $P(r_1)=\frac{1}{2}$, $P(r_2)=\frac{1}{2}$ for Player 1 and $P(c_1)=\frac{1}{2}$, $P(c_2)=\frac{1}{2}$ for Player 2. Can it converge to the pure-strategy Nash equilibrium by fictitious play? Or converge to mixed-strategy Nash equilibrium? Please justify your answer.

#### Q8.(10%) Battle of the Sexes
It is a two-player coordination game with different utility functions. Different from pure-coordination game, one player is happier than the other in any Nash equilibrium. See the following game matrix
|           | $c_1$ | $c_2$ |
|:---------:|:-----:|:-----:|
| **$r_1$** | (3,2) | (0,0) |
| **$r_2$** | (0,0) | (2,3) |

There co-exists two pure-strategy and one mixed-Strategy Nash equilibria. Can it converge to the pure-strategy Nash equilibria by fictitious play? Or converge to mixed-strategy Nash equilibrium? Please justify your answer.

#### Q9.(10%) Stag Hunt Game
One main characteristic is that one pure-strategy Nash equilibrium is the best for all but not other Nash equilibria. It differs from the prisoner's dilemma in that there are two pure-strategy Nash equilibria: one where both players cooperate, and one where both players defect. One famous application is the power control game. See the following game matrix
|           | $c_1$ | $c_2$ |
|:---------:|:-----:|:-----:|
| **$r_1$** | (3,3) | (0,2) |
| **$r_2$** | (2,0) | (1,1) |

There exists three Nash equilibria as well, including two pure-strategy Nash equilibria, i.e. $(r_1,c_1)$ and $(r_2,c_2)$, and one mixed-strategy Nash equilibrium, i.e. $P(r_1)=\frac{1}{2}$, $P(r_2)=\frac{1}{2}$ and $P(c_1)=\frac{1}{2}$, $P(c_2)=\frac{1}{2}$. Can it converge to the pure-strategy Nash equilibria by fictitious play? Or converge to mixed-strategy Nash equilibrium? Please justify your answer.

#### Q10.(10%) Observation and Conclusion
According to the observation based on above results, fictious play is still a useful iterative algorithm for us to find out the Nash equilibrium no matter pure-strategy or mixed-strategy. However, is it reliable to find Nash equilibrium by fictious play for every game matrices? If yes, please explain your reason in detail to justify it. If no, please provide a concrete counter-example.

:::info
:bulb: **Hint:** [powerpoint](https://people.cs.nctu.edu.tw/~lhyen/game/non_coop_game.pdf) in this course.
:::

---
## 4. Scoring Criteria

You will need to meet the requirements and answer the questions (marked with **"Q1 to Q10"**) in section 3 to write down a report. Please attach your screenshot of source code in your report and explain it in detail. Please do not put all your source code in the end of report. In general, we don’t test your code individually. As long as it is found that there is no source code in your report, then we'll check and test it one by one.

> :mag_right: For Q1 to Q10: each question contributes 10%. Answers to each question will be classified into one of the following four reward tiers: 
:one: excellent (10%): All goals achieved beyond expectation, including result screenshot, source code and clear explanation.
:two: good (6%): Some goals adequately achieved, such as only write down the result without any attachment or just attached picture with few explanation etc.
:three: normal (3%): Minimum goals achieved with major flaws, such as inaccurate answer with correct details or attachment without any explanation etc.
:four: fail (0%): Not graded due to no answer or other reasons, including ridiculous answer, wrong question number and non-executable program in our environment etc.

:::danger
:warning: **Attention**. You will get *NO POINT* when
* late work including any modification after the deadline.
* do not follow the submission rule including file name and format.
* cheating including any suspected plagiarism in source code or report.
:::

---
## 5. Submission
#### a. Pack your report, source code, and other relative files.
All your files should be organized in the following hierarchy and zipped into a .zip file, named ID_HW1.zip,  where ID is your student ID, e.g. 312551XXX_HW1.zip.

Directory structure inside the zipped file:
```
ID_HW1.zip (root)
|_ID_code(.cpp/.py/.m)
|_ID_report.pdf
|_...(optional)
```

---
## 6. References
[1] George W. Brown. Some notes on computation of Games Solutions. RAND Corporation Report P-78, April 1949.
[2] Julia Robinson. An iterative method of solving a game. The Annals of Mathematics, 54(2):296–301, 1951.
[3] Algorithmic Game Theory, by Noam Nisan, Tim Roughgarden, Eva Tardos, Vijay V. Vazirani (eds.), Cambridge University Press, September 2007.
[4] L. Shapley. Some topics in two-person games. Princeton University Press, 1964
[5] D. Monderer and A. Sela, Fictitious play and no-cycling conditions, mimeo, The Technion, 1997.
[6] D. Monderer and L.S. Shapley, Potential games, Games Econ. Behav. 14 (1996) 124-143.
[7] Berger, U. (2007) "Brown's original fictitious play", Journal of Economic Theory 135:572–578
[8] D. Monderer and L.S. Shapley, Fictitious play property for games with identical interests, J. Econ. Theory 68 (1996) 258-265.


