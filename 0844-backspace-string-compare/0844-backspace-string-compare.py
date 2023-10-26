class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(string):
            res = []
            for ch in string:
                if ch != "#":
                    res.append(ch)
                elif res:
                    res.pop()
            return "".join(res)
                    
        new_s = helper(s)
        new_t = helper(t)
        
        if new_s == new_t:
            return True
        else:
            return False
        
                    
        