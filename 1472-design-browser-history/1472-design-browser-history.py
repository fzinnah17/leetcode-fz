class LinkedList:
    def __init__(self, curr_val, nextNode = None, prevNode = None):
        #currval
        self.curr_val = curr_val
        #next
        self.nextNode = nextNode
        #prev
        self.prevNode = prevNode
        #creating a new linked list
    
class BrowserHistory(object):
    
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.page = LinkedList(homepage) #google.com 
        
    def visit(self, url):
        '''google.com, inserted url'''
        newNode = LinkedList(url) #initialize first visiting the url then I am assigning the arrows
        newNode.prevNode = self.page #google.com
        self.page.nextNode = newNode #twitter.com
        self.page = self.page.nextNode #make my current page twitter??
        
        # self.page.next = newNode #google's next page is twitter
        #twitter.com is a new node it has the node itself and it has the previous node which is Google.com to a new url yahoo.com

    def back(self, steps):
        """
        how many times >0
        """
        while self.page.prevNode and steps > 0:
            self.page = self.page.prevNode #twitter to google
            steps -= 1
        return self.page.curr_val #twitter's current value
        
        
    def forward(self, steps):
        """
        how many times
        """
        while self.page.nextNode and steps > 0:
            self.page = self.page.nextNode
            steps -= 1
        return self.page.curr_val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)