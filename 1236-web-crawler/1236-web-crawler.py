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
        ans = []
        same = startUrl.split('://')[1].split('/')[0]
        
        def dfs(url):
            childrens = htmlParser.getUrls(url)

            if url in visited:
                return
            ans.append(url)
            visited.add(url)
            for children in childrens:
                if children.split('://')[1].split('/')[0] != same:
                    continue
                dfs(children)
          #What happens if is not the same
        dfs(startUrl)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #remove the 0th index
        #visited
        #make all the connections and discard it
        #return ans
        
        
#         visited = set()
#         same = startUrl.split('://')[1].split('/')[0] 
#         ans = []
#         def dfs(node):
#             visited.add(node)
#             children = htmlParser.getUrls(node)
#             ans.append(node)
#             for i in children:
#                 if (i not in visited) and (i.split('://')[1].split('/')[0]) == same:
#                     dfs(i)
#         dfs(startUrl)
#         return ans
#         same = "http://example.org/test"
#         # same = same.rsplit('://')[1]
#         # additional = same.split('/')[0]
#         same = same.split('//')[1].split('/')[0]
        
#         print(same)
        # print(additional)