class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        #simulating to use stack and queue without using any of these
        Plan:
        1. Count 1's and 0's from student array
        2. iterate through the sandwiches array[as stack has a limitation to move around, but students can be moved anywhere for being in the queue]
            a. if current sandwich element is circle
                i. If circle students > 0, decrement circle student count
                ii. else: if it is == 0: break out the logic because idk
            b. If current sandwich element is square:
                i. If square student > 0, decement square student count
                ii. Else break out of the logic
        3. Return total left (1's + 0's) --> Unfed student
        Jonathan's way
        """
        circle_students = 0
        square_students = 0
        
        for i in range(len(students)):
            if students[i] == 0:
                circle_students += 1
            else:
                square_students += 1
        for j in range(len(sandwiches)):
            if sandwiches[j] == 0:
                if circle_students > 0:
                    circle_students -= 1
                else:
                    break
            else:
                if square_students > 0:
                    square_students -= 1
                else:
                    break
        return square_students + circle_students
    
        