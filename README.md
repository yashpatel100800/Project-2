# Longest String Chain Algorithm

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

