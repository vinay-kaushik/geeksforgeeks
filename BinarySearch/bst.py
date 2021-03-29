class bstNode:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data):
        # Check if root is available or not
        if self.data is None:
            self.data=data

        # If given data == existing data return it
        if self.data==data:
            return

        # insert logic
        # if given value is less than root, insert in the left node
        if data<self.data:
            if self.left:
                self.left.insert(data)
                return
            self.left=bstNode(data)
            return
        else:
            if self.right:
                self.right.insert(data)
                return
            self.right=bstNode(data)
            return

    def inorder(self,val_list):
        if self.left:
            self.left.inorder(val_list)
        if self.data:
            val_list.append(self.data)
        if self.right:
            self.right.inorder(val_list)
        
        return val_list

    def preorder(self,val_list):
        if self.data:
            val_list.append(self.data)
        if self.left:
            self.left.preorder(val_list)

        if self.right:
            self.right.preorder(val_list)
        
        return val_list
    def postorder(self,val_list):
        if self.left:
            self.left.postorder(val_list)

        if self.right:
            self.right.postorder(val_list)
        if self.data:
            val_list.append(self.data)
        
        return val_list

    def getMinimumElement(self):
        cur=self
        while cur.left:
            cur=cur.left
        return cur.data

    def getMaximumElement(self):
        cur=self
        while cur.right:
            cur=cur.right
        return cur.data



nums=[2,5,1,67,33,55,23,56,8,8,21]
print("Given nums list = ",nums)
binary_search_tree=bstNode()

for num in nums:
    binary_search_tree.insert(num)

print("insertion working")

print("Inorder traversal = ",binary_search_tree.inorder([]))
            
print("Preorder traversal = ",binary_search_tree.preorder([]))
print("Postorder traversal = ",binary_search_tree.postorder([]))
print("Minimum Element in the tree =",binary_search_tree.getMinimumElement())
print("Maximum Element in the tree =",binary_search_tree.getMaximumElement())
