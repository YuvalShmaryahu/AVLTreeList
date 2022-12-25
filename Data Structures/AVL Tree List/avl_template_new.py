# username - hadassayar
# id1      - 208581702
# name1    - Yuval Shmaryahu
# id2      - 209058510
# name2    - Hadas Sayar
import printree
from random import randint




class AVLNode(object):
    """A class represnting a node in an AVL tree"""
    """
    Constructor, you are allowed to add more fields.
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
        """
        Represents nodes of type AVLNode in O(1)
        @rtype: str
        @returns: Value of the node, "None" if it is a virtual node
        """
        if self.isRealNode():
            return str(self.value)
        else:
            return "virt"

    def getLeft(self):
        """
        returns the left child in O(1)
        @rtype: AVLNode
        @returns: the left child of self, None if there is no left child
        """
        if self.left.isRealNode():
            return self.left
        return self.left

    def getRight(self):
        """
        returns the right child in O(1)
        @rtype: AVLNode
        @returns: the right child of self, None if there is no right child
        """
        if self.right.isRealNode():
            return self.right
        return self.right

    def getParent(self):
        """
        returns the parent of a node in O(1)
        @rtype: AVLNode
        @returns: the parent of self, None if there is no parent
        """
        return self.parent

    def getValue(self):
        """
        return the value in O(1)
        @rtype: str
        @returns: the value of self, None if the node is virtual
        """
        if self.isRealNode():
            return self.value
        return None

    def getHeight(self):
        """
        returns the height in O(1)
        @rtype: int
        @returns: the height of self, -1 if the node is virtual
        """
        return self.height

    def setLeft(self, node):
        """
        sets left child in O(1)
        @type node: AVLNode
        @param node: a node
        """
        self.left = node
        return None

    def setRight(self, node):
        """
        sets right child in O(1)
        @type node: AVLNode
        @param node: a node
        """
        self.right = node
        return None

    def setParent(self, node):
        """
        sets parent in O(1)
        @type node: AVLNode
        @param node: a node
        """
        self.parent = node
        return None

    def setValue(self, value):
        """
        sets value in O(1)
        @type value: str
        @param value: data
        """
        self.value = value
        return None

    def setHeight(self, h):
        """
        sets the height of the node in O(1)
        @type h: int
        @param h: the height
        """
        self.height = h
        return None

    def setSize(self, size):
        """
        Sets the size of a node in O(1)
        @type size: int
        @param size: The size
        """
        self.size = size
        return None

    def getSize(self):
        """
        Gets the size of a node in O(1)
        @param self: AVLNode
        """
        return self.size

    def min(self):
        """
        Gets the minimum node in O(log(n))
        @param self: AVLNode
        """
        node = self
        while (node.left.value != None):
            node = node.left
        return node

    def max(self):
        """
        Gets the maximum node in O(log(n))
        @param self: AVLNode
        """
        node = self
        while (node.right.value != None):
            node = node.right
        return node

    def getPredecessor(self):
        """
        Returns the predecessor of a node in O(log(n))
        @type self: AVLNode
        @param self: A node
        @returns: The predecessor of the node
        """
        if self.left.value is not None:
            return self.left.max()
        x = self
        y = x.getParent()
        while (y is not None and x == y.getLeft()):
            x = y
            y = x.parent
        return y

    def getSuccessor(self):
        """
        Returns the predecessor of a node in O(log(n))
        @type self: AVLNode
        @param self: A node
        @returns: The predecessor of the node
        """
        if self.right.value is not None:
            return self.right.min()
        x = self
        y = x.getParent()
        while (y is not None and x == y.getRight()):
            x = y
            y = x.parent
        return y

    def isRealNode(self):
        """
        Checks if self is not a virtual node in O(1)
        @type self: AVLNode
        @param self: a node
        @rtype: bool
        @returns: False if self is a virtual node, True otherwise.
        """
        if self.getHeight() != -1:
            return True
        else:
            return False

    def getBalanceFactor(self):
        """
        Returns the balance factor of the node in O(1)
        @type self: AVLNode
        @param self: a node
        @rtype: int
        @returns: the Balance factor of self
        """
        return self.left.getHeight() - self.right.getHeight()

class AVLTreeList(object):
    """
    A class implementing the ADT list, using an AVL tree.
    """
    """
    Constructor, you are allowed to add more fields.
    """
    virtual = AVLNode(None)
    virtual.setSize(0)
    virtual.setHeight(-1)

    def getTreeHeight(self):
        return self.getRoot().getHeight()

    def append(self, val):
        return self.insert(self.length(), val)

    def __init__(self):
        """
        Constructor, you are allowed to add more fields.
        Initializes an empty list in O(1)
        """
        self.root = self.virtual
        self.counter = 0
        self.firstItem = None
        self.lastItem = None

    def __repr__(self):
        """
        Representation of the tree
        @return: Prints tree to console using printree
        function from Extended Introduction to CS course
        """
        out = ""
        for row in printree.printree(self):
            out = out + row + "\n"
        return out

    def select(self, i):
        """
        Returns the node of rank i in the tree in O(log(i))
        @type i: int
        @param i: rank of the node
        @rtype: AVLNode
        @return: The node of rank i in the tree
        """
        if self.empty():
            return None
        if i > self.getRoot().getSize():  # check if the rank exist
            return None
        return self.Tree_select_rec(self.root, i)

    def Tree_select_rec(self, node, i):
        """
        Recursive help method for select
        """
        leftTreeSize = node.left.size + 1
        if i == leftTreeSize:
            return node
        if (i < leftTreeSize):
            return self.Tree_select_rec(node.left, i)
        return self.Tree_select_rec(node.right, i - leftTreeSize)

    def empty(self):
        """
        returns whether the list is empty
        @rtype: bool
        @return: True if the list is empty, False otherwise
        """
        if self.getRoot() == None:
            return True
        return False

    def getTreeRoot(self):
        """Returns the root of the tree in O(1)
        @rtype: AVLNode
        @return: The root
        """
        return self.root

    def getVirtualNode(self):
        """
        Initiate a virtual node in O(1)
        @rtype AVLNode
        @return: Virtual node
        """
        virtual = AVLNode(None)
        virtual.setSize(0)
        virtual.setHeight(-1)
        return virtual

    def retrieve(self, i):
        """
        retrieves the value of the i'th item in the list in O(log(n))
        @type i: int
        @pre: 0 <= i < self.length()
        @param i: index in the list
        @rtype: str
        @returns: the value of the i'th item in the list
        """
        if self.getRoot() == None:
            return None
        if i < 0 :
            return None
        if i > self.getRoot().getSize() - 1:
            return None
        val = self.select(i + 1).value
        return val

    def insert(self, i, val):
        """
        inserts val at position i in the list in O(log(n))
        @type i: int
        @pre: 0 <= i <= self.length()
        @param i: The intended index in the list to which we insert val
        @type val: str
        @param val: the value we insert
        @rtype: list
        @return: the number of rebalancing operation due to AVL rebalancing
        """
        if(self.empty()):
            self.root = AVLNode(val)
            self.root.setSize(1)
            self.root.setHeight(0)
            virt = self.getVirtualNode()
            self.root.setLeft(virt)
            self.root.setRight(virt)
            virt.setParent(self.getRoot())
            return 0
        z = AVLNode(val)
        virtual = self.getVirtualNode()
        z.setLeft(virtual)
        z.setRight(virtual)
        virtual.setParent(z)
        if i == self.length():
            x = self.lastNode()
            x.setRight(z)
            z.setParent(x)
        else: # i < len(lst)
            x = self.select(i+1)
            if x.left.isRealNode() == False:
               # x.getLeft().setParent(z)
                x.setLeft(z)
                z.setParent(x)
            else: #x has left child
                y = x.getPredecessor()
                y.setRight(z)
                z.setParent(y)
                return self.fix_and_rotate(y)
        return self.fix_and_rotate(x)

    def delete(self, i):
        """
        deletes the i'th item in the list in O(log(n))
        @type i: int
        @pre: 0 <= i < self.length()
        @param i: The intended index in the list to be deleted
        @rtype: int
        @return: the number of rebalancing operation due to AVL rebalancing
        """
        if self.getRoot() == None:
            return -1
        if i > self.length() - 1:
            return -1
        if i <0:
            return -1
        x = self.select(i+1)
        #Deleting like BST tree
        if x.left.isRealNode() == False and x.right.isRealNode() == False: #x has no children (only virtual)
            if self.getRoot() == x:
                virtroot = self.getVirtualNode()
                self.setRoot(virtroot)
                return 0
            a = x.getParent()
            if a.getRight() == x:
                virt = self.getVirtualNode()
                a.setRight(virt)
                virt.setParent(a)
                self.fixSizeDelete(a)
                self.updateParentsHeightDelete(a)
            else:
                virt = self.getVirtualNode()
                a.setLeft(virt)
                virt.setParent(a)
                self.fixSizeDelete(a)
                self.updateParentsHeightDelete(a)
        elif x.left.isRealNode() and x.right.isRealNode() == False: # x has only left child
            x.setValue(x.getLeft().getValue())
            virt = self.getVirtualNode()
            x.setLeft(virt)
            virt.setParent(x)
            self.fixSizeDelete(x)
            self.updateParentsHeightDelete(x)
            a=x
        elif x.right.isRealNode() and x.left.isRealNode() == False: #x has only right child
            x.setValue(x.right.value)
            virt = self.getVirtualNode()
            x.setRight(virt)
            virt.setParent(x)
            self.fixSizeDelete(x)
            self.updateParentsHeightDelete(x)
            a=x
        else: # x has two children
            y = x.getSuccessor()
            p = y.getParent()
            x.setValue(y.getValue())
            if y.right.isRealNode():
                y.setValue(y.getRight().getValue())
                virt = self.getVirtualNode()
                y.setRight(virt)
                virt.setParent(y)
                self.fixSizeDelete(y)
                self.updateParentsHeightDelete(y)
                a=y
            else:
                if (y.getParent().getLeft() == y):
                    virt = self.getVirtualNode()
                    y.getParent().setLeft(virt)
                    virt.setParent(y.getParent())
                else:
                    virt = self.getVirtualNode()
                    y.getParent().setRight(virt)
                    virt.setParent(y.getParent())
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
                    self.counter += 1
                    self.right_rotation(a)
                else:
                    cntRotations += 2
                    self.counter += 2
                    self.left_rotation(a.getLeft())
                    self.right_rotation(a)
            elif bf == -2: #bf = -2
                if a.getRight().getBalanceFactor() == -1 or a.getRight().getBalanceFactor() == 0:
                    cntRotations += 1
                    self.counter += 1
                    self.left_rotation(a)
                else:
                    cntRotations += 2
                    self.counter += 2
                    self.right_rotation(a.getRight())
                    self.left_rotation(a)
            a = c
        self.firstItem = self.firstNode()
        self.lastItem = self.lastNode()
        return cntRotations

    def first(self):
        """
        returns the value of the first item in the list in O(log(n))
        @rtype: str
        @return: the value of the first item, None if the list is empty
        """
        if self.empty():
            return None
        return self.firstNode().getValue()

    def last(self):
        """
        returns the value of the last item in the list in O(log(n))
        @rtype: str
        @return: the value of the last item, None if the list is empty
        """
        if self.empty():
            return None
        return self.lastNode().getValue()

    def firstNode(self):
        """
        returns the first node in the list in O(log(n))
        @rtype: AVLNode
        @return: the first node, None if the list is empty
        """
        node = self.root
        if self.empty():
            return None
        elif node.left == None:
            return node
        else:
            while node.left.value != None:
                node = node.left
            return node

    def lastNode(self):
        """
        returns the last node in the list in O(log(n))
        @rtype: AVLNode
        @return: the last node, None if the list is empty
        """
        node = self.root
        if self.empty():
            return None
        elif node.right == None:
            return node
        else:
            while node.right.value != None:
                node = node.right
            return node

    def listToArray(self):
        """
        returns an array representing list in O(n)
        @rtype: list
        @return: a list of strings representing the data structure
        """
        if self.root.getSize() == 0:
            return []
        array = [0] * self.root.size
        node = self.root.min()
        for i in range(self.root.size):
            array[i] = node.value
            node = node.getSuccessor()
        return array

    def length(self):
        """
        returns the size of the list in O(1)
        @rtype: int
        @returns: the size of the list
        """
        return self.root.size

    def sort(self):
        """
        sort the info values of the list in O(nlog(n))
        @rtype: list
        @returns: an AVLTreeList where the values are sorted by the info of the original list.
        """
        tree = AVLTreeList()
        if self.root.getSize() == 0:
            return tree
        array1 = self.listToArray()
        array = self.mergesort(array1)
        for i in range (self.root.getSize()):
            tree.insert(i,array[i])
        return tree


    def concat(self, lst):
        """
        concatenates lst to self in O(log(n))
        @type lst: AVLTreeList
        @param lst: a list to be concatenated after self
        @rtype: int
        @returns: the absolute value of the difference between the height of the AVL trees joined
        """
        if lst.empty() and self.empty():
            return 0
        if self.empty():
            self.setRoot(lst.getRoot())
            return lst.getRoot().getHeight() + 1
        if lst.empty():
            return self.getRoot().getHeight() + 1
        a = self.getRoot()
        size1 = a.getSize()
        h1 = a.getHeight()
        h2 = lst.getRoot().getHeight()
        x = AVLNode(19534687821)
        if h1 < h2:
            new_root = self.joinleft(lst,x)
            self.setRoot(new_root)
        elif h1 > h2:
            self.joinright(lst, x)

        else:
            x.setRight(lst.getRoot())
            lst.getRoot().setParent(x)
            x.setLeft(self.getRoot())
            self.getRoot().setParent(x)
            x.setHeight(max(x.getLeft().getHeight(), x.getRight().getHeight()) + 1)
            x.setSize(x.getLeft().getSize() + x.getRight().getSize() + 1)
            self.setRoot(x)
        self.delete(size1)
        self.firstItem = self.firstNode()
        self.lastItem = self.lastNode()
        return abs(h1-h2)

    def joinright(self,lst,x):
        """
        Joins self, x, lst in O(height(lst) - height(self) + 1), where height(self) <= height(lst)
        @type x: AVLNode
        @type h: int
        @param x: node
        @rtype: AVLNode
        @returns: The root of the tree
        """
        a = lst.getRoot()
        h2 = a.getHeight()
        b = self.getRoot()
        while (b.getHeight()>h2):
            b = b.getRight()
        c = b.getParent()
        c.setRight(x)
        x.setParent(c)
        x.setRight(a)
        a.setParent(x)
        x.setLeft(b)
        b.setParent(x)
        self.balanceheightandsize(x)
        a = x
        while a != None:
            c = a.getParent()
            a.setHeight(max(a.left.getHeight(), a.right.getHeight()) + 1)
            bf = a.getBalanceFactor()
            if (bf == 1 or bf == -1) and a.getParent()==None:
                return lst.getRoot()
            if bf == 2:
                c = a.getParent()
                if a.getLeft().getBalanceFactor() == 1 or a.getLeft().getBalanceFactor() ==0:
                    self.counter += 1
                    self.right_rotation(a)
                else:
                    self.counter += 2
                    self.left_rotation(a.getLeft())
                    self.right_rotation(a)
            elif bf == -2: #bf = -2
                if a.getRight().getBalanceFactor() == -1 or a.getRight().getBalanceFactor() == 0:
                    self.counter += 1
                    self.left_rotation(a)
                else:
                    self.counter += 2
                    self.right_rotation(a.getRight())
                    self.left_rotation(a)
            a = c
        return self.getRoot()

    def joinleft(self,lst,x):
        """
        Joins self, x, lst in O(height(self) - height(lst) + 1), where height(lst) <= height(self)
        @type x: AVLNode
        @type h: int
        @param x:node
        @rtype: AVLNode
        @returns: The root of the tree
        """
        a = self.getRoot()
        h1 = a.getHeight()
        b = lst.getRoot()
        while (b.getHeight()>h1):
            b = b.getLeft()
        c = b.getParent()
        c.setLeft(x)
        x.setParent(c)
        x.setRight(b)
        b.setParent(x)
        x.setLeft(a)
        a.setParent(x)
        self.balanceheightandsize(x)
        a = x
        while a != None:
            c = a.getParent()
            a.setHeight(max(a.left.getHeight(), a.right.getHeight()) + 1)
            bf = a.getBalanceFactor()
            if (bf == 1 or bf == -1) and a.getParent()==None:
                return lst.getRoot()
            if bf == 2:
                c = a.getParent()
                if a.getLeft().getBalanceFactor() == 1 or a.getLeft().getBalanceFactor() ==0:
                    self.counter += 1
                    self.right_rotation(a)
                else:
                    self.counter += 2
                    self.left_rotation(a.getLeft())
                    self.right_rotation(a)
            elif bf == -2: #bf = -2
                if a.getRight().getBalanceFactor() == -1 or a.getRight().getBalanceFactor() == 0:
                    self.counter += 1
                    self.left_rotation(a)
                else:
                    self.counter += 2
                    self.right_rotation(a.getRight())
                    self.left_rotation(a)
            a = c
        return lst.getRoot()

    def makeNewTree(self, other):
        self.setRoot(other.getRoot())

    def search(self, val):
        """
        searches for a *value* in the list in O(n)
        @type val: str
        @param val: a value to be searched
        @rtype: int
        @returns: the first index that contains val, -1 if not found.
        """
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


    def getRoot(self):
        """
        returns the root of the tree representing the list in O(1)
        @rtype: AVLNode
        @return: the root, None if the list is empty
        """
        if self.root.getSize() == 0:
            return None
        return self.root

    def fixSize(self,node):
        """
        fixes the sizes of nodes all the way to the root by adding 1 to the size
         in O(log(n))
        @type self: AVLNode
        @param: a node after insert
        """
        tmp_node = node.parent
        while (tmp_node != None):
            tmp_node.size += 1
            tmp_node = tmp_node.parent

    def fixSizeDelete(self, node):
        """
        fixes the sizes of nodes all the way to the root by decresing 1 to the size
        in O(log(n))
        @type self: AVLNode
        @param: a node after delete
        """
        tmp_node = node
        while (tmp_node != None):
            prv_size = tmp_node.getSize()
            tmp_node.setSize(prv_size-1)
            tmp_node = tmp_node.getParent()

    def fix_and_rotate(self, node):
        """
        Rebalnces the AVL subtree after insert in O(1)
        @type node: AVLNode
        @param node: The root of the subtree
        @rtype: int
        @returns: number of rebalancing operations
        """
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
                    self.counter += 1
                # right rotation
            #    print("rotate right")
                self.right_rotation(node)
                cnt += 1
                self.counter += 1
                self.fixSize(node.parent)
                self.updateParentsHeight(node)
                return cnt
            node = node.getParent()
        self.firstItem = self.firstNode()
        self.lastItem = self.lastNode()
        return cnt

    def right_rotation(self,node):
        """
        Rotates the given subtree to the right in O(1)
        Using variables the same way as the lecture presentation. B has BF of +2 and A is its left child.
        Maintaining size and height attributions
        @type node: AVLNode
        @param node: The root of the subtree
        @rtype: AVLNode
        @returns: The root of the left rotated subtree
        """
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

    def left_rotation(self,node):
        """
        Rotates the given subtree to the left in O(1)
        Using variables the same way as the lecture presentation. B has BF of +2 and A is its left child.
        Maintaining size and height attributions
        @type node: AVLNode
        @param node: The root of the subtree
        @rtype: AVLNode
        @returns: The root of the left rotated subtree
        """
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
        """
        updates the parents' height after inserting a new node in O(log(n)),
        checking if the balancefactor is 0, if not - adding 1 to the height
        @type node: AVLNode
        @param node: The root of the subtree after insert
        """
        parent = node.parent
        while (parent != None):
            if (parent.getBalanceFactor() == 0):
                break;
            else:
                parent.height += 1
                parent = parent.parent

    def updateParentsHeightDelete(self,node):
        """
        updates the parents' height after deleting a node in O(log(n)),
        checking if the balancefactor is 0, if not - adding 1 to the height
        @type node: AVLNode
        @param node: The root of the subtree after insert
        """
        maxSubHeight = node.right.getHeight()
        if node.left.getHeight() > maxSubHeight:
            maxSubHeight = node.left.getHeight()
        node.setHeight(maxSubHeight +1)



    def setRoot(self,node):
        """
        sets a node as the tree root in O(1)
        @type node: AVLNode
        @param node: The root of the subtree after insert
        """
        self.root = node
        node.setParent(None)

    def merge(self,A, B):
        """
        merging two lists into a sorted list in O(nlog(n))
        A and B must be sorted!
        @param A, B: sorted lists
        @type A, B: list
        @rtype : list
        @return: a sorted list
        """
        n = len(A)
        m = len(B)
        C = [None for i in range(n + m)]
        a = 0;
        b = 0;
        c = 0
        while a < n and b < m:  # more element in both A and B
            if A[a] < B[b]:
                C[c] = A[a]
                a += 1
            else:
                C[c] = B[b]
                b += 1
            c += 1
        C[c:] = A[a:] + B[b:]  # append remaining elements (one of those is empty)
        return C

    def mergesort(self,lst):
        """
        recursive mergesort
         """
        n = len(lst)
        if n <= 1:
            return lst
        else:  # two recursive calls, then merge
            return self.merge(self.mergesort(lst[0:n // 2]),self.mergesort(lst[n // 2:n]))

    def permutation(self):
        """
        permute the info values of the list in O(n)
        @rtype: list
        @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
        """
        if self.root.getSize() == 0:
            return self
        if self.root.getSize() == 1:
            return self
        tree = AVLTreeList()
        array = self.listToArray()
        self.randomize(array, len(array))
        node = AVLNode(array[len(array) // 2])
        tree.setRoot(node)
        node.setLeft(self.getVirtualNode())
        node.setRight(self.getVirtualNode())
        node.setParent(None)
        node.setSize(len(array))
        h = self.createtreeinlineartime(array, True, node, 0, len(array) // 2 - 1) + self.createtreeinlineartime(
            array, False, node, len(array) // 2 + 1, len(array) - 1)
        self.height_fixer(tree)
        return tree

    def createtreeinlineartime(self,lst,bool,parent,first,last):
        """
        algorithm to create a tree in O(n) (like we sow on sorted array in recitation)
        @rtype node: AVLTreeList
        """
        index = (last+first +1)//2
        if last <first:
            return 0
        node = AVLNode(lst[index])
        node.setParent(parent)
        if parent!= None:
            if bool == True:
                parent.setLeft(node)
            else:
                parent.setRight(node)
        node.setSize(last-first+1)
        virtroot = self.getVirtualNode()
        node.setLeft(virtroot)
        node.setRight(virtroot)
        if (last-first +1 ==2):
            new_node =AVLNode(lst[first])
            virt = self.getVirtualNode()
            new_node.setLeft(virt)
            new_node.setRight(virt)
            virt.setParent(new_node)
            new_node.setParent(node)
            new_node.setSize(1)
            node.setLeft(new_node)
            return 1
        if (last-first +1 ==1):
            return 1
        return self.createtreeinlineartime(lst,True,node,first,index-1) + self.createtreeinlineartime(lst,False,node,index+1,last)

    def height_fixer(self,tree):
        """
        going to “leftist” node in the tree and update all of it’s parent heights in O(logn)
        """
        node = tree.firstNode()
        for i in range(self.root.size):
            node.setHeight(max(node.getLeft().getHeight(), node.getRight().getHeight()) + 1)
            node = node.getSuccessor()
        return None

    def randomize(self,arr, n):
        """
        function that returns a randomized array using Fisher Yates algorithm in O(n)
        @rtype: List
        @return: randomized array
        """
        for i in range(n - 1, 0, -1):
            j = randint(0, i + 1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr

    def balanceheightandsize(self,node):
        """
        balance height and size of node and all of its parent in O(logn)
        """
        while node != None:
            node.setHeight(max(node.getLeft().getHeight(),node.getRight().getHeight()) +1)
            node.setSize(node.getLeft().getSize() + node.getRight().getSize() +1)
            node = node.getParent()
