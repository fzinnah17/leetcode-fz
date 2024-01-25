class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map = collections.defaultdict(int)
        s2Map = collections.defaultdict(int)

        # Populate s1Map with the frequency of characters in s1
        for char in s1:
            s1Map[char] += 1

        l = 0
        r = 0

        # Iterate over s2 using a while loop
        while r < len(s2):
            # Add the current character to the s2Map
            s2Map[s2[r]] += 1

            # Check if the current window size is the same as s1
            if r - l + 1 == len(s1):
                if s1Map == s2Map:
                    return True

                # If the window is the right size, move left pointer to narrow the window
                s2Map[s2[l]] -= 1
                if s2Map[s2[l]] == 0:
                    del s2Map[s2[l]]
                l += 1

            r += 1

        return False
