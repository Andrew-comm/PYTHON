class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self,child):
        child.parent = self
        self.children.append(child)


    def print_tree(self):
        print(self.data)
        for child in self.children:
            print(child.data)


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("laptop")
    laptop.addChild(TreeNode("Hp"))
    laptop.addChild(TreeNode("Dell"))
    laptop.addChild(TreeNode("Mac"))


    cellphone = TreeNode("cellphone")
    cellphone.addChild(TreeNode("Tecno"))
    cellphone.addChild(TreeNode("Vivo"))
    cellphone.addChild(TreeNode("Samsung"))


    Tv = TreeNode("Tv")
    Tv.addChild(TreeNode("Dstv"))
    Tv.addChild(TreeNode("Gotv"))
    Tv.addChild(TreeNode("Smarttv"))

    root.addChild(laptop)
    root.addChild(cellphone)
    root.addChild(Tv)

    return root

    






if __name__ == '__main__':
    build_product_tree()
    root.print_tree()
    pass


