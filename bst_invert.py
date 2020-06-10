# Write a function that takes in a binary tree and inverts it.

# O(n) time || O(n) space


def invertBST(tree):
    # initialize queue
    queue = [tree]
    # while queue is not empty
    while len(queue):
        # current node is the first thing in the queue.
        # queue's follow first in first out method
        current = queue.pop(0)
        # if this is a leaf node, skip
        if current is None:
            continue
            # otherwise we need to swap it.
        swapLeftAndRight(current)
        # add the children nodes to the queue
        queue.append(current.left)
        queue.append(current.right)


def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left


# recursive solution
# O(n) time | O(d) space
def invert(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invert(tree.left)
    invert(tree.right)


def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left
