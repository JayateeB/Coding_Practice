class Node:

    def __init__(self,data):
        self.value = data
        self.leftchild = None
        self.rightchild = None

    def insert(self,data):
        if self.value == data:
            print("Data is already present in the binary search tree")
            return False
        if data < self.value:
            if self.leftchild:
                self.leftchild.insert(data)
            else:
                self.leftchild = Node(data)
        else:
            if self.rightchild:
                self.rightchild.insert(data)
            else:
                self.rightchild = Node(data)
        return True

    def search(self,data):
        if self.value == data:
            print(f"Value {data} is found")
            return True
        if data < self.value:
            if self.leftchild:
                return self.leftchild.search(data)
            else:
                print(f"Value {data} is not found")
                return False
        else:
            if self.rightchild:
                return self.rightchild.search(data)
            else:
                print(f"Value {data} is not found")
                return False

    def preorder(self):
        if self:
            print(self.value,end=" ")
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()

    def postorder(self):
        if self.leftchild:
            self.leftchild.postorder()
        if self.rightchild:
            self.rightchild.postorder()
        if self:
            print(self.value,end=" ")

    def inorder(self):
        if self.leftchild:
            self.leftchild.inorder()
        if self:
            print(self.value,end=" ")
        if self.rightchild:
            self.rightchild.inorder()


class Tree:

    def __init__(self):
        self.root = None

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
            return True
        else:
            self.root.insert(data)

    def search(self,data):
        if not self.root:
            print("Tree is empty")
            return False
        else:
            return self.root.search(data)

    def preorder(self):
        if not self.root:
            print("Tree is empty")
        else:
            print("\nPreorder traversal")
            self.root.preorder()

    def postorder(self):
        if not self.root:
            print("Tree is empty")
        else:
            print("\nPostorder traversal")
            self.root.postorder()

    def inorder(self):
        if not self.root:
            print("Tree is empty")
        else:
            print("\nInorder traversal")
            self.root.inorder()


if __name__ == '__main__':
    bst = Tree()
    bst.insert(5)
    bst.insert(8)
    bst.insert(3)
    bst.insert(19)
    bst.insert(45)
    bst.preorder()
    bst.postorder()
    bst.inorder()
    print(bst.search(5))



