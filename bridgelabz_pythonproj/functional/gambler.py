'''
/**********************************************************************************
* Purpose: Prints the harmonic value: 1/1 + 1/2 + ... + 1/N
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 21-12-2018
*
***********************************************************************************/
'''


from utilities import utility

stake = int(input("enter stake: "))
goal = int(input("enter goal: "))
turns = int(input("enter number of trials: "))


utility.gamblergame(stake,goal,turns)

