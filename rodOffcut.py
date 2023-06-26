"""
Perform the following steps repeatedly given an array of metal rod lengths:
1. Determine the number of rods.
2. Determine which rod(s) has the shortest length.
3. Throw away any rods of that length.
4. Take the shortest length of each of the longer rods and cut it. These are leftovers.
5. Remove all offcuts.
6. Continue until no more rods remain.
At the start of each round of actions, keep an array of the number of rods and return it.
For instance, n = 4 lengths = [1, 1, 3, 4]
• Because the shortest rods are only one unit long, discard them and record their length.
• Cut 1 unit of length from the longer rods and discard the offcuts.
• There are now two rods with lengths of [2, 3]. Remove the length 2 rod.
• Remove 2 from rod length 3 and discard the offcut.
• There is now only one rod of length one. Because it is the shortest, it is discarded.

Return an array containing the number of rods at the beginning of each turn: [4, 2, 1].
"""

def rodOffcut(lengths):
    output = []
    while len(lengths) > 0:
        output.append(len(lengths))
        min_length = min(lengths)
        lengths = [length - min_length for length in lengths if length > min_length]
    return output
