class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
The time complexity of this solution is O(n * m^2), where n is the number of books and m is the shelf width. This is because for every book, we potentially consider each width (up to the maximum shelf width) and height (up to the maximum shelf height). However, due to the memoization, we only compute each subproblem once. We are looping over all the books (n) in our input.
For each book, we could potentially have a different width and height, depending on whether we decide to add the book to the current shelf or start a new shelf. This is why we have the m^2 factor, where m is the maximum width.

The space complexity is O(n * m^2) as well, due to the memoization dictionary storing solutions to the subproblems. We might store a solution for every book at every possible width and height, which leads to the cubic space complexity. We are using a dictionary, 'memo', to remember the results of sub-problems we've already solved.
As with the time complexity, this dictionary could potentially store a result for every book at every possible width and height, which leads to the cubic space complexity.

        """
        memoTable = {}
        def dp(index, currWidth, currHeight):
            if index == len(books):
                return currHeight
            key = (index, currWidth, currHeight)
            if key in memoTable:
                return memoTable[key]
            width, height = books[index]
            if currWidth + width <= shelfWidth:
                firstOption = dp(index + 1, currWidth + width, max(currHeight, height))
            else:
                firstOption = float("inf")
            secondOption = currHeight + dp(index + 1, width, height)
            
            result = min(firstOption, secondOption)
            
            memoTable[key] = result
            return result
        return dp(0,0,0)
                
        