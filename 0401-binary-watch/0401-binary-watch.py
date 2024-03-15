class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        res = []
        leds = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]  # LED values for hours and minutes
        
        def dfs(idx, hours=0, minutes=0, count=0):
            if count > num or hours >= 12 or minutes >= 60:  # Early termination for invalid states
                return
            if count == num:
                res.append(f"{hours}:{minutes:02d}")
                return
            
            if idx < len(leds):  # Proceed only if there are LEDs left to process
                # If the LED is for hours (first 4 LEDs)
                if idx < 4:
                    dfs(idx + 1, hours + leds[idx], minutes, count + 1)  # LED turned on
                # If the LED is for minutes (last 6 LEDs)
                else:
                    dfs(idx + 1, hours, minutes + leds[idx], count + 1)  # LED turned on
                
                dfs(idx + 1, hours, minutes, count)  # LED turned off
        
        dfs(0)  # Start the recursion
        return res
