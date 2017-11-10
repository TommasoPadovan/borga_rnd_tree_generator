from tree import Tree

# edit this to change the number of nodes
NODE_NUMBER = 1000

# edit this to change the number of tries of your experiment
TRIES = 10

trees = [None] * TRIES

for t in range(0, TRIES):
    print ("starting try #%s..." % t)
    trees[t] = Tree()
    for i in range(1, NODE_NUMBER):
        trees[t].rnd_add()

    trees[t].in_order_visit()

    trees[t].post_order_visit()

Tree.output_csv_multiple(trees)
