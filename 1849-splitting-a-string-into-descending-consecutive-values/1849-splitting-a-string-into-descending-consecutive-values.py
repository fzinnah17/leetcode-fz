class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(index, prev):
            print(f"dfs called with index={index}, prev={prev}")
            if index == len(s):
                print("Reached end of string, returning True")
                return True
            
            for end in range(index + 1, len(s) + 1):
                num = int(s[index:end])
                print(f"Trying substring s[{index}:{end}] = {s[index:end]}, num = {num}")
                
                if prev is None:
                    if len(s) == end:  # Avoid considering the whole string as a start
                        print("Skipping whole string as start")
                        continue
                    print(f"First number in sequence: {num}, continuing search")
                    if dfs(end, num):
                        return True
                elif num + 1 == prev:
                    print(f"Found descending consecutive number: {num}, continuing search")
                    if dfs(end, num):
                        return True
                else:
                    print(f"{num} is not one less than {prev}, skipping")
                    
            print(f"No valid sequence from index {index}, returning False")
            return False
        
        return dfs(0, None)
