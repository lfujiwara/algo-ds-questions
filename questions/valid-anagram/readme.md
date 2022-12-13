# Valid Anagram

## Question
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Approach
By the defition, we know that two strings are anagrams if and only if they have the same number of occurences of each character (which implies that they have the same length). Therefore, if we sort their characters and then join them, we should get the same string if they are anagrams. Otherwise, they are not.

- Time complexity: O(nlogn)
    - Let n be the length of the longest string.
- Space complexity: O(n) for immutable strings, O(1) for mutable strings
    - If strings are mutable, we must sort them in place to get the O(1) space complexity.