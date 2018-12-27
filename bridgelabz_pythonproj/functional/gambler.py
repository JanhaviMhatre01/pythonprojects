'''
/**********************************************************************************
* Purpose: Simulates a gambler who start with $stake and place fair $1 bets until
* he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
* times he/she wins and the number of bets he/she makes. Run the experiment N
* times, averages the results, and prints them out.
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 22-12-2018
*
***********************************************************************************/
'''


from utilities import utility

stake = int(input("enter stake: "))     # take starting amount as stake
goal = int(input("enter goal: "))       # take final amount to win
turns = int(input("enter number of trials: "))  # number of trials


utility.gambler_game(stake, goal, turns)

