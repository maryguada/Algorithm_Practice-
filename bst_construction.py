# write a BST class for a BST. The class should support :
# A) Inserting values with the insert method
# B) Removing values with the remove methodl this method should
#   only remove the first instance of a given value.
# C) Searching for values with the contains method.

# BST: typically  it is made up of nodes.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# On Average: # O (log(n)) Time | O(1) space

    def insert(self, value):
        # initialize & find out what node youre at
        currentNode = self
        # until we hit a break statement
        while True:
            if value < currentNode.value:  # if value we are trying to insert is less than the currentNode.value
                # explore the left subtree.
                # base case: if left subtreee is empty.
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    # if currentnode is not None/null, we need to ecplore the left subtree.
                    currentNode = currentNode.left

            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    def contains(self, value):
        # initialize what node you're in.
        currentNode = self

        while currentNode is not None:
            # if the contains value that we are looking for is less than that of currentNode.value
            if value < currentNode.value:
                # keep going left until we find the contains value
                currentNode = currentNode.left
            # "contains strictly"
            elif value > currentNode.value:
                currentNode = currentNode.right

            else:
                return True  # This means that we found the value, return true
        # The BST does not contain that the value we are looking for.
        return False

    def remove(self, value, parentNode=None):
        # initialize your current node.
        currentNode = self
        # we have to think about edgecases.
        # root node to remove.
        # grab the smallest value in the right subtree. Grab the smallest value in the right subtree and put it ontop, kind of like finding "median"
        while currentNode is not None:
            # find the value we are trying to remove
            if value < currentNode.value:
                # parent node acts like a temp. We need to keep track of it bec the root route needs to be
                # replaced
                parentNode = currentNode
                # move the current node from root(Parent) to currentNode.left
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                # move right bc we need to explore the right subtree.
                currentNode = currentNode.right
            else:
                # 1st EDGECASE: when we are dealing with a node that has two children nodes.
                # Step One: find the smallest val of the right subtree.
                # if children are not none.
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    # at this point, currentNode.value = smallest value of the right subtree (which will be in the leftmost part of the right subtree we are exploring).
                    # we can remove that smallest val of right subtree now by calling the remove function.
                    # the currentNode that is second parameter to this, is the parentnode.
                    currentNode.right.remove(currentNode.value, currentNode)

                # 2nd EDGECASE: if we are trying to remove ROOT NODE of BST.
                    # ---- remember that root node does not have a parent node.
                elif parentNode is None:
                    if currentNode.left is not None:
                        # we have to do this in order.
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        # assign current node.left last so you don't loose it.
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.left
                        # assign current node last.
                        currentNode.left = currentNode.left.right
                    else:
                        # if no children node. We are essentially deleting the BST.
                        currentNode.value = None

                # 3rd EDGECASE: we are at a node that DOES NOT have two children:
                # check if node is the left child OR right child.
                elif parentNode.left == currentNode:
                    # when we know that this is now is the left child.therefore, #
                    # the parentnode.left is going to be reassigned to the left child or right child.
                    # parentnode.left
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                    # the same logic applies to the right child node.

                elif parentNode.right == currentNode:
                    # we are re-assigning the child of the parent node.
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right

                break

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            # traverse the left side of the tree.
            currentNode = currentNode.left
        return currentNode.value
