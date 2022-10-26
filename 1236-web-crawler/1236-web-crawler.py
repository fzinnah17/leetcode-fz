# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        visited = set()
        same = startUrl.split('://')[1].split('/')[0]
        ans = []
        def dfs(node):
            visited.add(node)
            children = htmlParser.getUrls(node)
            ans.append(node)
            for i in children:
                if (i not in visited) and (i.split('://')[1].split('/')[0]) == same:
                    dfs(i)
        dfs(startUrl)
        return ans
        