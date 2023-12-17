class Solution:
    MOD = 1000000007

    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        n = len(prevRoom)
        tree = [[] for _ in range(n)]

        # Building the tree from the room dependencies
        for i in range(1, n):
            tree[prevRoom[i]].append(i)

        # Array to store the size of each subtree
        subtree_size = [0] * n

        # DFS to calculate the size of each subtree with memoization
        def dfs(node):
            if subtree_size[node] != 0:
                return subtree_size[node]
            size = 1
            for child in tree[node]:
                size += dfs(child)
            subtree_size[node] = size
            return size

        # Calculating the factorial of n
        n_fact = 1
        for i in range(2, n + 1):
            n_fact = (n_fact * i) % self.MOD

        # Calculating the product of the sizes of all subtrees
        product_of_sizes = 1
        for i in range(n):
            product_of_sizes = (product_of_sizes * dfs(i)) % self.MOD

        # Calculating the modular inverse of the product of sizes
        def mod_inverse(a, m):
            return pow(a, m - 2, m)

        return (n_fact * mod_inverse(product_of_sizes, self.MOD)) % self.MOD
