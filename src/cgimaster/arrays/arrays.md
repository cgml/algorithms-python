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