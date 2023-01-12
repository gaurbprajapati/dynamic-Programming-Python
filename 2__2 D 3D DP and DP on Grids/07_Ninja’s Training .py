'''
A Ninja has an ‘N’ Day training schedule. He has to perform one of these three activities (Running, Fighting Practice, or Learning New Moves) each day. There are merit task associated with performing an activity each day. The same activity can’t be performed on two consecutive days. We need to find the maximum merit task the ninja can attain in N Days.

We are given a 2D Array task of size ‘N*3’ which tells us the merit activity of specific activity on that particular day. Our task is to calculate the maximum number of merit task that the ninja can earn.

'''


# recursive solution


def solverec(day, task, last):
    if (day == 0):
        maxi = -1
        for i in range(0, 3):
            if (i != last):
                maxi = max(maxi, task[0][i])
        return maxi

    maxi = -1
    for i in range(0, 3):
        if(i != last):
            activity = task[day][i]+solverec(day-1, task, i)
            maxi = max(maxi, activity)
    return maxi


# Memo Code

def solveMemo(day, task, last, dp):
    if (day == 0):
        maxi = -1
        for i in range(0, 3):
            if (i != last):
                maxi = max(maxi, task[0][i])
        return maxi

    if dp[day][last] != -1:
        return dp[day][last]

    maxi = -1
    for i in range(0, 3):
        if(i != last):
            activity = task[day][i]+solveMemo(day-1, task, i, dp)
            maxi = max(maxi, activity)
        dp[day][last] = maxi
    return dp[day][last]


# Tabulation

def SolveTabulation(day, task, last, dp):
    dp[0][0] = max(task[0][1], task[0][2])
    dp[0][1] = max(task[0][0], task[0][2])
    dp[0][2] = max(task[0][0], task[0][1])
    dp[0][3] = max(task[0][0], max(task[0][1], task[0][2]))

    for DaY in range(1, day+1):
        for LasT in range(4):
            for TasK in range(3):
                if(TasK != LasT):
                    activity = dp[DaY-1][TasK] + task[DaY][TasK]
                    dp[DaY][LasT] = max(dp[DaY][LasT], activity)
    return dp[day][last]


def solveSpaceOptimization(day, task, last, prev):
    prev[0] = max(task[0][1], task[0][2])
    prev[1] = max(task[0][0], task[0][2])
    prev[2] = max(task[0][0], task[0][1])
    prev[3] = max(task[0][0], max(task[0][1], task[0][2]))

    for DaY in range(1, day+1):
        temp = [-1 for i in range(3+1)]
        for LasT in range(4):
            for TasK in range(3):
                if(TasK != LasT):
                    activity = prev[TasK] + task[DaY][TasK]
                    temp[LasT] = max(temp[LasT], activity)
        prev = temp

    return prev[last]


task = [[10, 40, 70],
        [20, 50, 80],
        [30, 60, 90]
        ]
n = len(task)

dp = [[-1 for i in range(3+1)] for j in range(n+1)]

print(solverec(n-1, task, 3))
print(solveMemo(n-1, task, 3, dp))
print(SolveTabulation(n-1, task, 3, dp))

prev = [-1 for i in range(3+1)]


print(solveSpaceOptimization(n-1, task, 3, prev))
