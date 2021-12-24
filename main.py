#Practicing Binary Trees

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def TreePrinter(self, traversal_type):
        if traversal_type == "preorder":
            return self.PreOrder(tree.root, "")
        elif traversal_type == "inorder":
            return self.InOrder(tree.root, "")
        else:
            print(str(traversal_type) + " Not Supported, try all lowercase or different traversal type")
            return False

    def PreOrder(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.PreOrder(start.left, traversal)
            traversal = self.PreOrder(start.right, traversal)
        return traversal

    def InOrder(self, start, traversal):
        if start:
            traversal = self.InOrder(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.InOrder(start.right, traversal)
        return traversal





tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.right.right = Node(5)


print(tree.TreePrinter("inorder"))
print(tree.TreePrinter("preorder"))
