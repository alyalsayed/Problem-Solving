# Bulb Switch Problem

### Link :

https://leetcode.com/problems/bulb-switcher/


Given n bulbs that are initially off, you first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

The problem is to find how many bulbs are on after n rounds.

## Solutions

Here are three different solutions to the problem:

### Solution 1: Brute Force

The brute force solution iterates through all the bulbs from 1 to n, and toggles the state of each bulb for each round. At the end of the n rounds, the state of each bulb is checked, and the number of bulbs that are on is returned. Here's the Python code for this solution:

```python
def bulbSwitch(n: int) -> int:
    bulbs = [False] * n
    for i in range(1, n+1):
        for j in range(i-1, n, i):
            bulbs[j] = not bulbs[j]
    return sum(bulbs)
```
This solution has a time complexity of O(n^2), because it iterates through all the bulbs for each round.

### Solution 2: Math
The math solution counts the number of integers from 1 to n that have an odd number of factors. This can be done by counting the number of integers whose prime factorization has an odd exponent for at least one prime factor. Here's the Python code for this solution:

```python
import math

def bulbSwitch(n: int) -> int:
    return int(math.sqrt(n))
```

This solution has a time complexity of O(1), because it only calculates the integer square root of n.

### Solution 3: Optimization

The optimized solution takes advantage of the pattern in the bulb states to avoid iterating through all the bulbs for each round. it iterates over the square numbers up to the square root of n and increments a counter for each square number that is less than or equal to n. This is because a bulb with index i is toggled k times if and only if i is a perfect square and k is a factor of i. Therefore, we only need to consider the perfect squares less than or equal to n. Here's the Python code for this solution:

```python
import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        count = 0
        for i in range(1, int(math.sqrt(n))+1):
            if i * i <= n:
                count += 1
        return count
```
This solution has a time complexity of O(n^(1/2)), because it iterates through all the integers from 1 to n, and checks if each integer is a perfect square.

Conclusion
In this problem, we saw three different solutions with varying time complexities. The math solution is the most efficient with a time complexity of O(1), but it requires knowledge of number theory. The optimized solution has a time complexity of O(n^(1/2)), which is better than brute force, but it is still not as efficient as the math solution. The brute force solution is the least efficient with a time complexity of O(n^2), but it is the simplest to understand and implement.

In general, it is important to consider the time complexity of a solution when solving algorithmic problems, especially for large input sizes. However, it is also important to balance efficiency with simplicity and readability, as complex solutions can be difficult to maintain and debug.

