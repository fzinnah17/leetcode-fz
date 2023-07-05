"""
Given an array of meeting times return the minimum number of conference rooms required.
Input: array = [[0,30],[25,10],[5,20]]
Output: 2
"""
class Solution:
    def minMeetingRooms(array):
        """
        Pseudocode:
        1. Two lists: start = [], end = [] and have the values inserted
            [0,5,15] [10,20,30]
        2. Two pointers, variables: room = 0
        3. if end 10 > start 0: start += 1, room += 1 min room
           if end 10 < start 15: end += 1, room -= 1 min room
        4. return the room
        TC: O(N) & SC: O(N)
        """
        start, end = [],[]
        for nums in intervals:
            start.append(nums[0])
            end.append(nums[1])
        start.sort()
        end.sort()
        left, right = 0, 0
        maxRoom = 0
        room = 0
        while left < len(start) and right < len(end):
            if end[right] > start[left]: #no overlapping because two meetings can still happen simultaneously without requiring an additional room
                left += 1
                room += 1
            else:
                right += 1
                room -= 1
            maxRoom = max(maxRoom,room)
        return maxRoom
