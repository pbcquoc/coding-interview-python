class BSTNode:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None
        
    def insert(self, key):
        if self.key == key:
            self.count += 1
        elif key < self.key:
            if self.left == None:
                self.left = BSTNode(key)
            else:
                self.left.insert(key)
        else:
            if self.right == None:
                self.right = BSTNode(key)
            else:
                self.right.insert(key)

    def inorder(self):
        if self.left != None:
            self.left.inorder()
        print((self.key, self.count), end=' ')
        if self.right != None:
            self.right.inorder()

class BSTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root == None:
            self.root = BSTNode(key)
        else:
            self.root.insert(key)

    def inorder(self):
        if self.root != None:
            self.root.inorder()


bstree = BSTree()
arr = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
print(arr)
for i in arr:
    bstree.add(i)
bstree.inorder()


