class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        1. How to access strings inside a list?   ------> for loop in (len(strs))
        2. How to access character counts in those strings?  -----> Counter
        ** It is inside a list, so I have to iterate thru the list once to count the number of occurences in each string
        """
        l = []
        d = {}
        c = {}
        for i in strs:
            a = Counter(i)
            if a in l:
                for j,k in c.items():
                    if k == a:
                        d[j] += [i]
            else:
                d[i] = [i]
                l.append(a)
                c[i] = a
        return d.values()