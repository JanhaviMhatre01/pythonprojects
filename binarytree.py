'''
/**********************************************************************************
* Purpose: Possible Number of Binary Search Tree

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 5-1-2019
*
***********************************************************************************/
'''


def bst(nodes):  # code is based on catalan number formula [ 2n!/((n+1)! * n!) ]
    # catalan number formula is used in counting problems
    # calculation of 2n!
    f1 = 1
    for i in range(1, (2 * nodes) + 1):
        f1 = f1 * i

    # calculation of (n+1)!
    f2 = 1
    for i in range(1, (nodes + 1) + 1):
        f2 = f2 * i

    # calculation of n!
    f3 = 1
    for i in range(1, nodes + 1):
        f3 = f3 * i

    result = f1 // (f2 * f3)  # [ 2n!/((n+1)! * n!) ]
    print("number of possible binary trees ", result)


try:
    nodes = int(input("Enter number of nodes :"))
    bst(nodes)
except ValueError:
    print("Enter value in int format")
