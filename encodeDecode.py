"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Example 1:

Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]
Output: [""]

TC: O(n) SC: O(n)
"""
def encode(self, strs: List[str]) -> str:
    """Encodes a list of strings to a single string.
    ["Farnaz", "F.ate4ma", Zin3nah"]
    "6.Farnaz8F.ate4ma7Zin3nah"
    """
    res = ""
    for c in strs:
        res += str(len(c)) + "." + c
    return res
    

def decode(self, s: str) -> List[str]:
    """Decodes a single string to a list of strings.
    s = "6.Farnaz8F.ate4ma7Zin3nah"
    """
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != ".":
            j += 1
        length = int(s[i:j])
        res.append(s[j+1:j+1+length])
        i = j + 1 + length
    return res
