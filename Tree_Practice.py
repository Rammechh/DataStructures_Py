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
            print(root.data)
            self.traverse_Inorder(root.right)
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

tree.traverse_Inorder(root)
