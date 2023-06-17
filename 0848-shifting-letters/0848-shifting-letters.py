class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        TC: O(n) SC: O(n)
        """
        sum_of_shifts = sum(shifts)
        result = []
        for i in range(len(s)):
            curr_char = s[i]
            shift = (ord(curr_char) - ord('a') + sum_of_shifts) % 26
            new_char = chr(ord('a') + shift)
            sum_of_shifts = (sum_of_shifts - shifts[i]) % 26
            result.append(new_char)
        return "".join(result)
        