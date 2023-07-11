class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        TC: O(n) SC: O(1)
        """
        while sandwiches and sandwiches[0] in students:
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
            else:
                currStudent = students.pop(0)
                students.append(currStudent)
        return len(students)
        