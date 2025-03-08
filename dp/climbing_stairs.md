#### Climbing Stairs

You are given an integer n representing the number of steps to reach the top of a staircase. 

You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.


Here is the solution below:

```
def Solution(n: int):
    """
    :param n:
    :return:
    """
    if n <= 1:
        return 1

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1  # Base cases

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
```