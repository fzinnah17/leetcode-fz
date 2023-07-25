from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        def prereqMap(givenCourses):
            reqMap = defaultdict(list)
            for course in givenCourses:
                key = course[0]  # course needs to be taken
                val = course[1]  # course acting as a prereq
                reqMap[key].append(val)
            return reqMap  # Return the reqMap dictionary instead of printing it

        courseMap = prereqMap(prerequisites)

        def hasCycle(courseNum, visited, path):
            if courseNum in path:
                return True  # Cycle detected
            
            if courseNum in visited:
                return False
            
            visited.add(courseNum)
            path.add(courseNum)
            
            for preReq in courseMap[courseNum]:
                if hasCycle(preReq, visited, path):
                    return True
            
            path.remove(courseNum)
            return False

        for courseNum in range(numCourses):
            if hasCycle(courseNum, set(), set()):
                return False

        return True
