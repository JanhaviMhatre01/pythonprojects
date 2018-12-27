'''
/**********************************************************************************
* Purpose: User Input and Replace String Template “Hello <<UserName>>, How are you?”
* logic:-taking user input for username and replacing
*        <<username>> with user entered username
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 21-12-2018
*
***********************************************************************************/
'''
from utilities import utility

username = input("enter username: ")  # take username from user to replace with <<username>>

utility.username_change(username)