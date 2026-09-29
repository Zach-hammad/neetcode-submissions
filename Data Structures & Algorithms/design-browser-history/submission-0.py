class ListNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = ListNode(homepage)


    def visit(self, url: str) -> None:
        node, next, prev = ListNode(url), None, self.homepage
        node.next = next
        node.prev = prev
        prev.next = node
        self.homepage = node

    def back(self, steps: int) -> str:
        cur = self.homepage
        while cur.prev and steps > 0:
            cur = cur.prev
            steps-=1
        self.homepage = cur
        return self.homepage.url
        

    def forward(self, steps: int) -> str:
        cur = self.homepage
        while cur.next and steps>0:
            cur = cur.next
            steps-=1
        self.homepage = cur
        return self.homepage.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)