# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info
import printree
import random
"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        self.height = 0

    def __repr__(self):
        if self.isRealNode():
            return self.value
        else:
            return "virt"

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    # O(1)
    def getLeft(self):

        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    # O(1)
    def getRight(self):

        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    # O(1)
    def getParent(self):
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    # O(1)
    def getValue(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    # O(n)
    def getHeight(self):
        return self.height

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        self.left = node




    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node


    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        self.value = value

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h





    """Sets the size of a node in O(1)
            @type size: int
            @param size: The size
            """
    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size


    def min(self):
        node = self
        while (node.left.value != None):
            node = node.left
        return node

    def max(self):
        node = self
        while (node.right.value != None):
            node = node.right
        return node

    def getPredecessor(self):
        if self.left.value is not None:
            return self.left.max()
        node = self
        y = node.parent
        while (y is not None and x == y.left):
            x = y
            y = x.parent
        return y

    def getSuccessor(self):
        if self.right.value is not None:
            return self.right.min()
        node = self
        y = node.parent
        while (y is not None and x == y.right):
            x = y
            y = x.parent
        return y

    # O(1)
    def isRealNode(self):
        if self.getHeight() != -1:
            return True
        else:
            return False

    def getBalanceFactor(self):
        return self.left.getHeight() - self.right.getHeight()


    # Updating the height of a node
    def setRealHeight(self):
        if (self.right.value == None):
            self.height = self.left.height + 1
            return self.height
        if (self.left.value == None):
            self.height = self.right.height + 1
            return self.height
        else:
            self.height = 1 + max(self.left.height, self.right.height)
            return self.height


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.
    """
    virtual = AVLNode(None)
    virtual.setSize(0)
    virtual.setHeight(-1)

    def __init__(self):
        self.root = self.virtual

    def __repr__(self):
        """Representation of the tree
        @returns: Prints tree to console using printree
        function from Extended Introduction to CS course
        """
        out = ""
        for row in printree.printree(self):
            out = out + row + "\n"
        return out
    # add your fields here

    ##return a node by its rank
    def select(self, i):
        return self.Tree_select_rec(self.root, i)

    def Tree_select_rec(self, node, i):
        leftTreeSize = node.left.size + 1
        if i == leftTreeSize:
            return node
        if (i < leftTreeSize):
            return self.Tree_select_rec(node.left, i)
        return self.Tree_select_rec(node.right, i - leftTreeSize)

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.root.value == None

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """
    def getTreeRoot(self):
        """Returns the root of the tree in O(1)
        @rtype: AVLNode
        @returns: The root
        """
        return self.root
    def getVirtualNode(self):

        return self.virtual

    def retrieve(self, i):
        val = self.select(i + 1).value
        return val

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, i, val):
        if(self.empty()):
            self.root = AVLNode(val)
            self.root.setSize(1)
            self.root.setHeight(0)
            self.root.setLeft(self.getVirtualNode())
            self.root.setRight(self.getVirtualNode())
            return 0
        z = AVLNode(val)
        z.setLeft(self.getVirtualNode())
        z.setRight(self.getVirtualNode())
        if i == self.length():
            x = self.lastNode()
            x.setRight(z)
            z.setParent(x)
        else: # i < len(lst)
            x = self.select(i+1)
            if x.left.isRealNode() == False:
                x.setLeft(z)
                z.setParent(x)
            else: #x has left child
                y = x.getPredecessor()
                y.setRight(z)
                z.setParent(y)
                return self.fix_and_rotate(y)
        return self.fix_and_rotate(x)



    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        x = self.select(i+1)
        #Deleting like BST tree
        if x.left.isRealNode() == False and x.right.isRealNode() == False: #x has no children (only virtual)
            if self.getRoot() == x:
                self.setRoot(self.getVirtualNode())
                return 0
            a = x.getParent()
            if a.getRight() == x:
                a.setRight(self.getVirtualNode())
                self.fixSizeDelete(a)
                self.updateParentsHeightDelete(a)
            else:
                a.setLeft(self.getVirtualNode())
                self.fixSizeDelete(a)
                self.updateParentsHeightDelete(a)
        elif x.left.isRealNode() and x.right.isRealNode() == False: # x has only left child
            x.setValue(x.getLeft().getValue())
            x.setLeft(self.getVirtualNode())
            self.fixSizeDelete(x)
            self.updateParentsHeightDelete(x)
            a=x
        elif x.right.isRealNode() and x.left.isRealNode() == False: #x has only right child
            x.setValue(x.right.value)
            x.setRight(self.getVirtualNode())
            self.fixSizeDelete(x)
            self.updateParentsHeightDelete(x)
            a=x
        else: # x has two children
            y = x.getSuccessor()
            p = y.getParent()
            x.setValue(y.getValue())
            if y.right.isRealNode():
                y.setValue(y.getRight().getValue())
                y.setRight(self.getVirtualNode())
                self.fixSizeDelete(y)
                self.updateParentsHeightDelete(y)
                a=y
            else:
                if (y.getParent().getLeft() == y):
                    y.getParent().setLeft(self.getVirtualNode())
                else:
                    y.getParent().setRight(self.getVirtualNode())
                self.fixSizeDelete(p)
                self.updateParentsHeightDelete(p)
                a=p
        #AVL rebalancing
        cntRotations = 0
        while a != None:
            c = a.getParent()
            a.setHeight(max(a.left.getHeight(),a.right.getHeight()) + 1)
            bf = a.getBalanceFactor()
            if (bf == 1 or bf == -1) and a.getParent()==None:
                return cntRotations
            if bf == 2:
                c = a.getParent()
                if a.getLeft().getBalanceFactor() == 1 or a.getLeft().getBalanceFactor() ==0:
                    cntRotations += 1
                    self.right_rotation(a)
                else:
                    cntRotations += 2
                    self.left_rotation(a.getLeft())
                    self.right_rotation(a)
            elif bf == -2: #bf = -2
                if a.getRight().getBalanceFactor() == -1 or a.getRight().getBalanceFactor() == 0:
                    cntRotations += 1
                    self.left_rotation(a)
                else:
                    cntRotations += 2
                    self.right_rotation(a.getRight())
                    self.left_rotation(a)
            a = c
        print(self)
        return cntRotations



    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        if self.empty():
            return None
        return self.firstNode().getValue()

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        if self.empty():
            return None
        return self.lastNode().getValue()

    def lastNode(self):
        node = self.root
        if self.empty():
            return None
        elif node.right == None:
            return node
        else:
            while node.right.value != None:
                node = node.right
            return node

    def firstNode(self):
        node = self.root
        if self.empty():
            return None
        elif node.left == None:
            return node
        else:
            while node.left.value != None:
                node = node.left
            return node
    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        array = [0] * self.root.size

        node = self.root.min()
        for i in range(self.root.size):
            array[i] = node.value
            node = node.getSuccessor()
        return array

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return self.root.size

    """sort the info values of the list

    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    def sort(self):
        tree = AVLTreeList()
        array = self.listToArray()
        for i in range (self.root.size):
            tree.insert(i,array[i])
        return tree

    """permute the info values of the list 

    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    """

    def permutation(self):
        tree = AVLTreeList()
        array = self.listToArray()
        random.shuffle(array)
        for i in range(self.root.size):
            tree.insert(i, array[i])
        return tree

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        h1 = self.root.height
        h2 = lst.root.size
        if (h2 == h1):
            x = lst.first()
            lst.delete(x)
            x.setleft(self.root)
            x.setright(lst.root)
            return 0
        if(h2 > h1):
            x = lst.first()
            lst.delete(x) #we will use this x to join the 2 avl trees
            x.setleft(self.root) # the left child of x will be the root of the self avl (a in lucture)
            # finding b - the first node in lst that its height is <= self height
            b = lst.root
            while(b.height > h1):
                b = b.left
            c = b.parent
            x.setright(b) # the right child of x will be the root of the subtree in lst that its height <= h1
            c.setleft(x) #b's parent is now x's parent
            self.fix_and_rotate_left(c)
            return (h2 - h1)
        else: #h2 < h1
            x = self.last()
            self.delete(x)
            x.setleft(lst.root)
            # finding b - the first node in self that its height is <= lst height
            b = self.root
            while (b.height > h2):
                b = b.right
            c = b.parent
            x.setleft(b)  # the left child of x will be the root of the subtree in self that its height <= h2
            c.setright(x)  # b's parent is now x's parent
            self.fix_and_rotate_right(c)
            return (h1 - h2)


    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """


    def search(self, val):
        if self.empty() == True:
            return -1
        node = self.root
        while (node.left.value != None):
            node = node.left
        if node.value == val:
            return 0
        for i in range (self.root.size -1):
            node = node.getSuccessor()
            if node.value == val:
                return i + 1
        return -1

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """



    def getRoot(self):
        return self.root

    def fixSize(self,node):
        tmp_node = node.parent
        while (tmp_node != None):
            tmp_node.size += 1
            tmp_node = tmp_node.parent

    def fixSizeDelete(self, node):
        tmp_node = node
        while (tmp_node != None):
            prv_size = tmp_node.getSize()
            tmp_node.setSize(prv_size-1)
            tmp_node = tmp_node.getParent()
    def fix_and_rotate(self, node):
        if node == None:
            return 0
        while node != None:
            # update size and height of node
            node.setSize(1 + node.getLeft().getSize() + node.getRight().getSize())
            node.setHeight(1 + max(node.getLeft().getHeight(), node.getRight().getHeight()))
            cnt = 0  # counting rotates
            if (node.getBalanceFactor() < -1):# BF is -2 We should run a left rotation
                #Now if BF of right child is 1 we should have right rotation on the right child
                #and then left rotation on the node
                #print(self)
                #print(node, node.getBalanceFactor())
                if node.getRight().getBalanceFactor() == 1:

                    #right rotation on child

                    #print("rotate right than left")
                    node.setRight(self.right_rotation(node.getRight()))
                    # we set the right child of node to be the root of the subtree after rotation
                    cnt += 1
                #left rotation
                #print("rotate left")
                self.left_rotation(node)
                cnt += 1
                self.fixSize(node.parent)
                self.updateParentsHeight(node)
                return cnt

            elif node.getBalanceFactor() > 1: ## BF is 2 We should run a right rotation

                # Now if BF of right child is -1 we should have left rotation on the left child
                # and then right rotation on the node
             #   print(self)
              #  print(node, node.getBalanceFactor())
                if node.getLeft().getBalanceFactor() == -1:
                    indictor = True
                    # left rotation on child
                  #  print("rotate left than right")
                    node.setLeft(self.left_rotation(node.getLeft()))
                    # we set the Left child of node to be the root of the subtree after rotation
                    cnt += 1
                # right rotation
            #    print("rotate right")
                self.right_rotation(node)
                cnt += 1
                self.fixSize(node.parent)
                self.updateParentsHeight(node)
                return cnt
            node = node.getParent()

        return cnt

    # Using variables the same way as the lecture presentation. B has BF of +2 and A is its left child.
    def right_rotation(self,node):  # Maintaining size and height attributes
        B = node
        A = node.getLeft()
        isRoot = self.root == B
        B.setLeft(A.getRight())
        A.getRight().setParent(B)
        C = B.getParent()
        if not C == None:#B is not the root
            # B is left child
            if (C.getLeft() == B):
                C.setLeft(A)
            #B is right child
            if C.getRight() == B:
               C.setRight(A)
        A.setParent(C)
        A.setRight(B)
        A.setSize(B.getSize())
        B.setParent(A)
        #fix size and height
        B.setSize(B.left.getSize() + B.right.getSize() + 1)
        B.setHeight(max(B.left.getHeight(),B.right.getHeight()) + 1)
        A.setHeight(max(A.left.getHeight(), A.right.getHeight()) + 1)
        if isRoot:
            self.setRoot(A)
        return A #The root of the rotated subtree

    def left_rotation(self,node): # Maintaining size and height attributes
        B = node
        A = node.getRight()
        isRoot = self.root == B
        B.setRight(A.getLeft())
        A.getLeft().setParent(B)
        C = B.getParent()
        if not C == None:  # B is not the root
            # B is left child
            if C.getLeft() == B:
                C.setLeft(A)
            # B is right child
            if C.getRight() == B:
                C.setRight(A)
        A.setParent(C)
        A.setLeft(B)
        A.setSize(B.getSize())
        B.setParent(A)
        # fix size and height
        B.setSize(B.left.getSize() + B.right.getSize() + 1)
        B.setHeight(max(B.left.getHeight(), B.right.getHeight()) + 1)
        A.setHeight(max(A.left.getHeight(), A.right.getHeight()) + 1)
        if isRoot:
            self.setRoot(A)
        return A #The root of the rotated subtree



    def updateParentsHeight(self,node):
        parent = node.parent
        while (parent != None):
            if (parent.getBalanceFactor() == 0):
                break;
            else:
                parent.height += 1
                parent = parent.parent

    def updateParentsHeightDelete(self,node):
        maxSubHeight = node.right.getHeight()
        if node.left.getHeight() > maxSubHeight:
            maxSubHeight = node.left.getHeight()
        node.setHeight(maxSubHeight +1)



    def setRoot(self,node):
        self.root = node



