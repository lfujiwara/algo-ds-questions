# Two sum

## Question
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Approaches

### Approach 1: Brute Force
It's simple, iterate over each value, then for each of those values, iterate again on the remaining part of the array, check if the sum of the first value and the second one equals to target, if it does, return the indexes, otherwise, continue.

- Time complexity: O(n^2)
    - We iterate over the remaining array for every element, on average, the iteration size is around n/2, so the time complexity is O(n/2) * O(n) = O(n^2)
- Space complexity: O(1)
    - We don't use any extra just the iterators

### Approach 2: Hash table
Init a hash table and iterate over each element of the array, first check if the complement of the current element to target is in the table, if it is, return the indexes, otherwise, add the current element to the hash table with the key being the element and the value being the index.

- Time complexity: O(n)
    - We iterate over the array once, and for each element, we check if the complement is in the hash table, which takes O(1) time, so the time complexity is O(n)
- Space complexity: O(n)

### Approach 3: Sorting
Sort the array, then init two pointers, one at the beginning and one at the end, because the array is sorted, we know that if we move the left pointer forward, the sum will increase, and if we move the right pointer backward, the sum will decrease, so we can check if the sum is equal to target, if it is, return the indexes, if it's less than target, move the left pointer forward, otherwise, move the right pointer backward. Be sure that you can modify the array first.

- Time complexity: O(nlogn)
    - We sort the array first, which takes O(nlogn) time, then we iterate over the array once, so the time complexity is O(nlogn) + O(n) = O(nlogn)
- Space complexity: O(1)
