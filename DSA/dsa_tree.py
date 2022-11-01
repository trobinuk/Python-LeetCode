class TreeNode:
    def __init__(self,data):
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self,val):
        val.parent = self
        self.child.append(val)

    def add_parent(self):
        pass

    def print_data(self):
        spaces = " " * self.get_level()*2
        prefix = spaces+'|__' if self.parent else ''
        print(prefix+self.data)
        if len(self.child) > 0:
            #self.child.print_data()
            for i in self.child:
                i.print_data()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

def build_product_tree():
    root = TreeNode('Electronics')

    laptops = TreeNode('Laptops')
    cellphones = TreeNode('Cellphones')
    tv = TreeNode('Tv')

    root.add_child(laptops)
    root.add_child(cellphones)
    root.add_child(tv)

    #print(root.data)
    #print(root.child)

    laptops.add_child(TreeNode('Mac'))
    laptops.add_child(TreeNode('Lenova'))
    laptops.add_child(TreeNode('Dell'))

    cellphones.add_child(TreeNode('iPhone'))
    cellphones.add_child(TreeNode('Pixel'))

    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('Sony'))

    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_data()