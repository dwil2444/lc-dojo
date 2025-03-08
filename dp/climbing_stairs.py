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


if __name__ == '__main__':
    print(Solution(5))



