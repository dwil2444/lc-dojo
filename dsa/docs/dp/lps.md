# Longest Palindromic Substring (**LEETCODE MEDIUM**)
Given a string s, return the longest palindromic substring in s. 

Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:


Input: s = "cbbd"
Output: "bb"
```


## Why is this a Dynamic Programming Problem?  
- **Overlapping Subproblems** related to substrings of s. Specifically to check whether a substring `s[i...j]` is a palindrome, we can reuse
solutions of smaller substrings.
-   e.g if `s[i+1 ... j-1]` is a palindrome, then we only need to check if `s[i] == s[j]` to determine if `s[i...j]`is a palindrome.
- The same subproblem is solved multiple times during the execution, which can be optimized by storing the results of previously computed subproblems in a dp table.

2. **Optimal Substructure** as the solution can be built from solutions to smaller subproblems.

## DP Approach:
- State Definition:  Let `dp[i][j]` be a boolean value that indicates whether the substring `s[i...j]` is a palindrome.

- Recurrence Relation: `dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]`

- Base Cases: A single character is always a palindrome, so `dp[i][i]` = True $\forall i$

- Solution: The longest palindromic substring can be found by iterating through the `dp` table to find the largest `dp[i][j]` == True that represents a palindrome.    

#### Here is the solution below:

```
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        # DP table initialization
        dp = [[False] * n for _ in range(n)]
        start = 0  # To store the starting index of the longest palindromic substring
        max_len = 1  # At least one character is a palindrome

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check substrings of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1): 
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if length > max_len:
                            max_len = length
                            start = i

        return s[start:start + max_len]
```


## Time Complexity:
$O(n^{2})$ as the worst case for the outer and inner loops run for n iterations each.



## Space Complexity: 
$O(n^{2})$ as the DP table stores boolean values for all pairs.