## First Duplicate

Given an array a that contains only numbers in the range from 1 to a.length, 
find the first duplicate number for which the second occurrence has the minimal index. 
In other words, if there are more than 1 duplicated numbers, return the number for which 
the second occurrence has a smaller index than the second occurrence of the other number does. 
If there are no such elements, return -1.

```
Time: O(n)
Space: O(1)

For a = [2, 3, 3, 1, 5, 2], the output should be
first_duplicate(a) = 3.
```

## First Non-Repeating Character
Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you would be asked to do during a real interview.

Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.

There are no characters in this string that do not repeat.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string that contains only lowercase English letters.

Guaranteed constraints:
1 ≤ s.length ≤ 105.

[output] char

The first non-repeating character in s, or '_' if there are no characters that do not repeat.

## Rotate Image
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 100,
a[i].length = a.length,
1 ≤ a[i][j] ≤ 104.

[output] array.array.integer