class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def create_Node(self,data):
        return Node(data)
    
    def insert_Node(self,node,data):
        if node is None:
            return self.create_Node(data)
        elif data<node.data:
            node.left=self.insert_Node(node.left,data)
        else:
            node.right=self.insert_Node(node.right,data)
        return node
    
    def traverse_Inorder(self,root):
        if root is not None:
            self.traverse_Inorder(root.left)
            print(root.data, end=" ")
            self.traverse_Inorder(root.right)
    def traverse_preOrder(self,root):
        if root is not None:
            print(root.data, end=" ")
            self.traverse_Inorder(root.left)
            self.traverse_Inorder(root.right)
    def traverse_postOrder(self,root):
        if root is not None:
            self.traverse_Inorder(root.left)
            self.traverse_Inorder(root.right)
            print(root.data, end=" ")
#Driver Code 
tree=Tree()
root=tree.create_Node(5)
tree.insert_Node(root, 2)
tree.insert_Node(root, 10)
tree.insert_Node(root, 7)
tree.insert_Node(root, 15)
tree.insert_Node(root, 12)
tree.insert_Node(root, 20)
tree.insert_Node(root, 30)
tree.insert_Node(root, 6)
tree.insert_Node(root, 8)
print("roots inserted in order\n5 2 10 7 15 12 20 30 6 8")
print("Inorder")
tree.traverse_Inorder(root)
print("\nPreOrder")
tree.traverse_preOrder(root)
print("\nPostOrder")
tree.traverse_postOrder(root)

