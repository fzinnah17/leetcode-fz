class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        leds = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]  # LED values for hours and minutes

        def dfs(idx, hours, minutes, count):
            if hours >= 12 or minutes > 59:  # Skip invalid times
                return
            if count == num:  # If the count of lights matches the required number
                res.append(f"{hours}:{minutes:02d}")
                return
            if idx == len(leds):  # If all LEDs have been considered
                return
            
            # Include the current LED (turned on)
            if idx < 4:  # First 4 LEDs are for hours
                dfs(idx + 1, hours + leds[idx], minutes, count + 1)
            else:  # Next 6 LEDs are for minutes
                dfs(idx + 1, hours, minutes + leds[idx], count + 1)
            
            # Exclude the current LED (turned off)
            dfs(idx + 1, hours, minutes, count)
        
        dfs(0, 0, 0, 0)
        return res
