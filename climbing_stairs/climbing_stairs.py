# this is a fibonacci problem
def climbStairs(self, n: int) -> int:
    leftPosition = 1
    rightPosition = 1
    for number in range(n - 1):
        temp = leftPosition
        leftPosition = leftPosition + rightPosition
        rightPosition = temp
    return leftPosition


"""
5th step: 1 path
4th step: 1 path
3rd step: 2 paths
2nd step: 3 paths
1st step: 5 paths
from the start: 8 paths

if there were five steps, on the fifth step which is the right position, there is one path from there. from the fourth step there is also one path by taking one step to the fifth step. from the third step you can get to the fourth step (one path) or to the fifth step (also one path) which means there are two paths. From the second step you can get to the third step which has two paths and the fourth path which has one path. As a result from the second step you have three paths. From the first step you can get to either the second or third step which means you have five paths. From the starting you can get to the first step or the second step giving you a total of 8 paths. 

for five steps
[0,1,2,3,x,x]
iteration starts here
[0,1,2,x,x]: number = 0
[0,1,x,x]: number = 1
[0,x,x]: number = 2
[x,x]: number = 3
range(n-1)
"""
