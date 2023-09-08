"""
Given two strings s and t, return true if they are both one edit distance apart, otherwise, return false. A string s is said to be one distance apart from a string t if you can:
    a. Insert exactly one character into s to get t.
    b. Delete exactly one character from s to get t.
    c. Replace exactly one character of s with a different character to get t.

Example 1: Input: s = "ab", t = "acb", Output: true, Explanation: We can insert 'c' into s to get t.
Example 2: Input: s = "", t = "" Output: false Explanation: We cannot get t from s by only one step.
"""
def isOneEditDistance(self, s: str, t: str) -> bool:
    """
    1. Order Matters: order is crucial in this problem.
    2. Repetitive Characters: If you need to replace 'a' with 'b' in "aaabc", the frequency of characters matters.
    Length Check: Before checking the differences, check the lengths of the two strings. There are a few possibilities:
            a. If len(s) == len(t), then you should only have a replace operation available.
            b. If len(s) == len(t) + 1, then you should only have a delete operation in s.
            c. If len(s) + 1 == len(t), then you should only have a delete operation in t (or an insert in s).
            d. If the length difference is greater than 1, return false immediately.
    3. Iterative Check: Once you have the length conditions in place, iterate through the strings. If the lengths are the same, you should only have one mismatch. If the lengths differ by one, you should skip one character in the longer string and continue matching the rest.
    4. End of Strings: Be careful about reaching the end of one string before the other, especially if their lengths differ by 1. 
    TC: O(n) SC: O(1)
    """
    if s == t: #both same TC: O(1) SC: O(1)
        return False
    if abs(len(s) - len(t)) > 1:#as we are only allowed to make 1 edit TC: O(1) SC: O(1)
        return False
    i = 0
    j = 0
    diff = 0
    while i < len(s) and j < len(t): #TC: O(n), n is the length of the longer string, SC: O(1)
        if s[i] != t[j]:
            diff += 1
            if diff > 1:
                return False
            #s = "xy" t = "xyz" -> If a character needs to be added to s/deleted from t
            if len(s) < len(t):
                j += 1
            #s = "xyz" t = "xy" -> If a character needs to be added to t/deleted from s
            elif len(s) > len(t):
                i += 1
            else: #s = "xyz" t = "xyb" -> If a character needs to be replaced
                i += 1
                j += 1               
        else:
            i += 1
            j += 1
    return True
