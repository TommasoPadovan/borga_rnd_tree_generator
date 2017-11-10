from tree import Tree

# edit this to change the number of nodes
NODE_NUMBER = 1000

tree = Tree()

for i in range(1, NODE_NUMBER):
    tree.rnd_add()


tree.in_order_visit()

tree.post_order_visit()

tree.printTree()
