
# (Code 1) Zero Border Square Algorithm

This Python script implements an algorithm to find the largest square sub-matrix within a given matrix, where all the elements along the border are zeros. The script takes a matrix as input and returns the coordinates of the corner zeros of the largest square sub-matrix with a zero border, if it exists.

## How to Use

1. Ensure you have Python installed on your system.
2. Copy the provided Python script into a Python-compatible environment or a Python file.
3. Invoke the `contains_zero_square` function with a matrix (list of lists) as input.
4. The function returns a tuple containing a boolean value indicating whether a square sub-matrix with a zero border exists, and a list of tuples representing the coordinates of the corner zeros of the largest such square.

## Example Usage

```python
matrix = [
    [1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1]
]

result, corners = contains_zero_square(matrix)
print("Contains square with zero border:", result)
print("Indexes of corner zeros:", corners)
```

Output:
```
Contains square with zero border: True
Indexes of corner zeros: [(1, 0), (1, 3), (4, 0), (4, 3)]
{1, 5} {0, 4}
 , , , , , ,
0,0,0,0,0, ,
0, , , ,0, ,
0, , , ,0, ,
0, , , ,0, ,
0,0,0,0,0, ,
```

## Algorithm Explanation

1. The `contains_zero_square` function takes a matrix as input.
2. It defines a helper function `is_zero_square` that checks if a square sub-matrix of a given size, starting at a given row and column, satisfies the zero border condition.
3. The outer loops iterate over all possible starting positions (row, column) in the matrix.
4. For each starting position, the inner loop iterates over all possible square sizes from 2 to the maximum possible size, given the starting position.
5. The `is_zero_square` function checks if the corner elements and border elements of the square sub-matrix are zeros.
6. If a square sub-matrix with a zero border is found, the function returns `True` and a list of tuples representing the coordinates of the corner zeros of the largest such square.
7. If no such square is found, the function returns `False` and an empty list.

## Efficiency Analysis

- Time Complexity: O(n^4), where n is the size of the input matrix.
- Space Complexity: O(n^2), where n is the size of the input matrix.

## Note

- This algorithm assumes that the input matrix contains valid elements.
- The time complexity of this solution is high, and for large matrices, it may not be efficient enough. There might be better algorithms or optimizations to improve the time complexity for this problem.



# (Code 2) Longest String Chain Algorithm

This Python script implements an algorithm to find the longest string chain from a list of strings. A string chain is formed by removing one character at a time from a string to create a new string that is also present in the original list. The script sorts the input strings by length, then iterates through each string to determine its chain length and predecessor in the longest chain.

## How to Use:
1. Ensure you have Python installed on your system.
2. Copy the provided Python script into a Python-compatible environment or a Python file.
3. Invoke the `longest_string_chain` function with a list of strings as input.
4. The function returns the longest string chain found in descending order.

## Example Usage:

strings = ["abde", "abc", "abd", "abcde", "ade", "ae", "1abde", "abcdef"]

print(longest_string_chain(strings))  
Output: ["abcdef", "abcde", "abde", "ade", "ae"]

## Algorithm Explanation:
1. Sort the input strings by length.
2. Initialize dictionaries to store chain length and predecessors.
3. Iterate through each string:
   - Initialize chain length for the current string.
   - Try removing each character and check if resulting string is in the input list.
   - Update chain length and predecessor if a longer chain is found.
   - Update the maximum chain length and its end string.
4. Reconstruct the longest string chain using predecessors.
5. Return the longest string chain if its length is greater than 1.

## Efficiency Analysis:
- Time Complexity: O(n log n + n * m^2), where n is the number of strings and m is the maximum length of the strings.
- Space Complexity: O(n), where n is the number of strings.

## Note:
- This algorithm assumes that the input list contains valid strings.
- The algorithm prioritizes efficiency over simplicity, utilizing dynamic programming to optimize the solution.


