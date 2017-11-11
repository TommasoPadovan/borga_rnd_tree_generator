from tree import Tree
from parenthesis import tryAndFix

# edit this to change the number of nodes
NODE_NUMBER = 5

# edit this to change the number of tries of your experiment
TRIES = 10

trees = [None] * TRIES

# for t in range(0, TRIES):
#     print ("starting try #%s..." % t)
#     trees[t] = Tree()
#     for i in range(1, NODE_NUMBER):
#         trees[t].rnd_add()
#
#     trees[t].in_order_visit()
#
#     trees[t].post_order_visit()
#
# Tree.output_csv_multiple(trees)

tree = Tree()

tree.generate_from_pattern(tryAndFix(NODE_NUMBER))

tree.in_order_visit()

tree.post_order_visit()

print(tree.printTree())

tree.output_csv()
