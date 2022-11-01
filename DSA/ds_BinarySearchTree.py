class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):

        if data == self.data:
            return

        if data < self.data:
            #Add data in Left side of the Tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            #Add data in Right side of the Tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def inorder_traversal(self):
        elements = []

        #Values in Left Node
        if self.left:
            elements += self.left.inorder_traversal()

        #Values in the root Node
        elements.append(self.data)

        #Values in the right node
        if self.right:
            elements += self.right.inorder_traversal()
        
        return elements

    def search(self,val):
        if self.data == val:
            return True

        if val < self.data:
            # Search in Left side of the tree
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            # search in right side of the Tree
            if self.right:
                return self.right.search(val)
            else:
                return False
        

def build_binary_search_tree(inp_nums):

    root = BinarySearchTree(inp_nums[0])
    for i in range(1,len(inp_nums)):
        root.add_child(inp_nums[i])  

    #elements = root.inorder_traversal()
    return root

if __name__ == "__main__":
    nums = [7,18,4,25,62,10,2,12,140]
    built_tree = build_binary_search_tree(nums)
    print(built_tree) 

    built_tree.search(24)

    built_tree.search(25)

