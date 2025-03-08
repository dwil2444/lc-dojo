# Dynamic Programming

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems. 
It is mainly used to solve optimization problems.


## Problem:
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence goes 0, 1, 1, 2, 3, 5, 8, 13, and so on.

*Write a function fibonacci(n) that returns the nth number in the Fibonacci sequence.*


## Example: Fibonacci Sequence

The recursive formula to compute the Fibonacci sequence is as follows: $F_n = F(n-1) + F(n-2)$.


## Why is this a Dynamic Programming Problem?  
This problem is a classic example of overlapping subproblems, which is a key indicator that Dynamic Programming can optimize the solution.

- **Overlapping subproblems:** To compute fibonacci(5), you need to compute fibonacci(4) and fibonacci(3). But in the recursive approach, fibonacci(4) and fibonacci(3) will be recalculated multiple times.

- **Optimal substructure:** The Fibonacci sequence exhibits optimal substructure since the solution to the problem (fibonacci(n)) depends on the solutions to the smaller subproblems (fibonacci(n-1) and fibonacci(n-2)).

By storing the intermediate results of the subproblems we can avoid redundant calcualtions. This is done through memoization (storing results in a cache)
**or** tabulation (building up solutions in an iterative manner)

## Dynamic Programming Solution (Tabulation Approach)

```
def fibonacci(n):
    if n <= 1:
        return n

    # create a table to store Fibonacci values
    dp = [0] * (n + 1)

    # base cases
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

## Explanation of Tabulation Soliution:
1. Base Case: If n is 0 or 1 return n, because these are given as the first two numbers of the sequence.
2. DP Array: Create an array `dp` to store Fibonacci numbers from `0` to `n`. Initialize the frist two values of the array:
`dp[0]=0` and `dp[1]=1`.
3. Iterative Solution: Use a loop to fill the array for values from `2` to `n`. The value of each Fibonacci number is calculated as the 
sum of the two previous numbers `dp[i] = dp[i-1] + dp[i-2]`
4. Return the result: finally, return `dp[n]` which contains the nth Fibonacci Number.

## Time Complexity:
`O(n)` as we only need to compute each Fibonacci number once and store it in the array



## Space Complexity: 
`O(n)` due to the storage of the Fibonacci sequence in an array of size `n+1`.