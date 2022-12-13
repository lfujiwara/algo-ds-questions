# Contains Duplicate

## Question

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Approaches

### Approach 1: Naive
Iterate over each value, then iterate again, skipping the value previously selected, and check if there's a value that matches the first value. If there is, return true. If not, return false.

- Time complexity: O(n^2)
    - Each bottom-level (after first value is selected) takes O(n), and there are O(n) of them, so O(n^2).
- Space complexity: O(1)

### Approach 2: Sorting
If the array is sorted, then repeated values will be adjacent, so all you have to do is check, for each index (except the last one) if the value at that index is equal to the value at the next index. If it is, return true. If not, keep going. If you get to the end, return false.

- Time complexity: O(n log n)
    - Sorting takes on average O(n log n) (and worst case if using mergesort or similar), and then iterating over the array takes O(n), so O(n log n) + O(n) = O(n log n).
- Space complexity: O(1)

### Approach 3: Hash Table
Init a hash table, then iterate over each value, check if it's on the table, it is, return false, otherwise add it to the table. If you get to the end, return true.

- Time complexity: O(n)
    - Iterating over the array takes O(n), and checking if a value is on the table takes O(1), so O(n) + O(n) = O(n).
- Space complexity: O(n)
    - Hash tables generally occupy the size of the keys times a constant plus size of the values. Therefore it should be O(n), but beware of possibly huge constants that may arise for each implementation of a hash table.

Obs: Although not exactly optiomal, one could also use an ordered set, which would be O(log n) for insertion and search, therefore O(n log n) total, and still be O(n) for space complexity.
