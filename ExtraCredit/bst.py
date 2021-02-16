from __future__ import print_function

import inflect # convert number to english write


class Node(object):
    """Tree node: left and right child + data which can be any object

    """
    def __init__(self, data):
        """Node constructor

        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """Insert new node with data

        @param data node data object to insert
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        """Lookup node containing data

        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def delete(self, data):
        """Delete node containing data

        @param data node's content to delete
        """
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                # if node has no children, just remove it
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.data = None
            elif children_count == 1:
                # if node has 1 child
                # replace node by its child
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                else:
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data
            else:
                # if node has 2 children
                # find its successor
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                # replace node data by its successor data
                node.data = successor.data
                # fix successor's parent node child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def compare_trees(self, node):
        """Compare 2 trees

        @param node tree to compare
        @returns True if the tree passed is identical to this tree
        """
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if res is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.right.compare_trees(node.right)
        return res

    def display(self):
        lines, _, _, _ = self.print_tree()
        for line in lines:
            print(line)
    #  this new print_tree , it is better than previous
    def print_tree(self):
        """Print tree content inorder

        """
        # if self.left:
        #     self.left.print_tree()
        # print(self.data, end=" ")
        # if self.right:
        #     self.right.print_tree()

        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.print_tree()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.print_tree()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.print_tree()
        right, m, q, y = self.right.print_tree()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


    def tree_data(self):
        """Generator to get the tree nodes data

        """
        # we use a stack to traverse the tree in a non-recursive way
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                # we are returning so we pop the node and we yield it
                node = stack.pop()
                yield node.data
                node = node.right

    def children_count(self):
        """Return the number of children

        @returns number of children: 0, 1, 2
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
    ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

    # number to write , descending order using generator and yield
    liste = []

    def inOrder_(self):
        if self:
            if self.left :
                self.left.inOrder_()
            self.liste.append(self.data)
            if self.right:
                self.right.inOrder_()

    def descanding(self):
        self.inOrder_()
        p = inflect.engine()
        newList = sorted(self.liste)
        for i in newList[::-1]:
            yield p.number_to_words(i)
    # depth of tree
    def getHeight(self):
        return 1 + max(self.left.getHeight() if self.left is not None else 0,
                       self.right.getHeight() if self.right is not None else 0)


    def countNodes(self) :
        if self is None:
            return 0
        else:
            if self.left is not None  and self.right is not None :
                return self.left.countNodes() + self.right.countNodes() + 1
            elif self.left is None and self.right is not None :
                return self.right.countNodes() + 1
            elif self.right is  None and self.left is not None:
                return self.left.countNodes() + 1
            else :
                return 1


