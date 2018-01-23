class Tree:
    def __init__(self, root):
        self.root = Node(root)
        
	def insert(self, val):
        temp = self.root
        
        while temp.value()!=None:
            if val>temp.value():
                temp = temp.right()
            else:
                temp = temp.left()
                
        temp.setValue(val)


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None
        self.visited = False
        
        
    def __init__(self,key):
        self.left = Node()
        self.right = Node()
        self.val = key
        self.visited = False
 

	def right(self):
        return self.right
    
    def left(self):
        return self.left
    
    def isVisited(self):
        return self.visited
    
    def setRight(self, key):
        self.right = Node(key)
        
    def setLeft(self, key):
        self.left = Node(key)
        
    def setVisited(self, key):
        self.visited = key
        
    def value(self):
        return self.val
 	
    def setValue(self, key):
        if self.val==None:
            self.left = Node()
            self.right = Node()
        self.val = key
