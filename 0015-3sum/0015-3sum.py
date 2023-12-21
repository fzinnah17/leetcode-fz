class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Two pointers concept is used in: 
        a. Optimizing algorithms for processing large files or streams, like handling large JSON responses in a REST API.
        b. Optimizing memory usage in file uploads or streaming services.
        c. For example, when reading and parsing a large log file, you can use two pointers to keep track of the current position and process the file in chunks, reducing memory usage and improving performance.
        d.  Instead of loading the entire file into memory, you can use two pointers to read and process the file in smaller segments, reducing the memory footprint of your application.
        
        For this problem, it is used as: optimizing the search process and reducing unnecessary iterations, improving the performance of finding valid triplets.
        
        Pseudocode:
        1. Sort the input
        2. have two pointers one in the beginning and one after
        3. if the curr value == previous value then move the right pointer
        
        """
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            # Check if it's not the first element in the sorted array and if it's the same as the previous element.
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip the current iteration if it's a duplicate value.

            left = i + 1  # Initialize the left pointer to the next element.
            right = len(nums) - 1  # Initialize the right pointer to the last element.

            while left < right:
                curr = nums[left] + nums[right] + nums[i]  # Calculate the sum of three elements.

                if curr > 0:
                    right -= 1  # If the sum is greater than zero, move the right pointer to the left.

                elif curr < 0:
                    left += 1  # If the sum is less than zero, move the left pointer to the right.

                else:
                    res.append([nums[left], nums[right], nums[i]])  # If the sum is zero, it's a valid triplet.
                    left += 1
                    # Skip any consecutive duplicates on the left side of the array.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        # Return the list of valid triplets.
        return res
