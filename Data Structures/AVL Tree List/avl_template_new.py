# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info


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
        self.balanaceFactor = 0


    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    # O(1)
    def getLeft(self):
        if self.left.value == None:
            return None
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    # O(1)
    def getRight(self):
        if self.right.value == None:
            return None
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
        return None





    """Sets the size of a node in O(1)
            @type size: int
            @param size: The size
            """
    def setSize(self, size):

        self.size = size


    def min(self):
        node = self
        if node.value is None:
            return None
        while (node.left.value != None):
            node = node.left
        return node.value

    def max(self):
        node = self
        if node.value is None:
            return None
        while (node.right.value != None):
            node = node.right
        return node.value

    def getPredecessor(self):
        if self.left.value is not None:
            return max(self.left)
        node = self
        y = node.parent
        while (y is not None and x == y.left):
            x = y
            y = x.parent
        return y

    def getSuccessor(self):
        if self.right.value is not None:
            return min(self.right)
        node = self
        y = node.parent
        while (y is not None and x == y.right):
            x = y
            y = x.parent
        return y

    # O(1)
    def isRealNode(self):
        if self.value == None:
            return False
        return True

    def getBalanceFactor(self):
        return (self.left.height - self.right.height)

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


    # add your fields here

    ###    Yuval added from here
    ##return the rank of a node
    def select(self, i):
        return self.Tree_select_rec(self.root, i)

    def Tree_select_rec(self, node, i):
        r = node.left.size + 1
        if i == r:
            return node
        if (i < r):
            return self.Tree_select_rec(node.left, i)
        return self.Tree_select_rec(node.right, i - r)

    ### to here
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
            return self.fix_and_rotate_right(x)
        else: # i < len(lst)
            x = self.select(i+1)
            if x.left.val == None:
                x.setleft(z)
                return self.fix_and_rotate_left()
            else: #x has left child
                y = x.predecessor
                y.setright(z)
                return self.fix_and_rotate_right()



    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        x = self.select( i)
        a = x.parent
        prv_h = a.Height
        #Deleting like BST tree
        if x.left.value == None and x.right.value == None: #x has no children
            x.setValue(None)
        elif x.left.value != None and x.right.value == None:
            x.setValue(x.left.value)
            x.left.setValue(None)
        elif x.right.value != None and x.left.value == None:
            x.setValue(x.right.value)
            x.right.setValue(None)
        else:
            y = x.getSuccessor()
            x.setValue(y.value)
            y.setValue(y.right.value)
            y.right.setValue(None)
        self.updateParentsHeight(a)
        #AVL rebalancing
        cntRotations = 0
        while a.value != None:
            bf = a.getBalanceFactor
            if bf < 2 and bf >-2:
                now_h = a.Height
                if now_h == prv_h:
                    return 0
                else:
                    a = a.parent
            elif bf == 2:
                cntRotations += self.fix_and_rotate_right(a)
                a = a.parent
            else: #bf = -2
                cntRotations += self.fix_and_rotate_left(a)
                a = a.parent



    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        node = self.root
        if self.empty():
            return None
        while node.left.value is not None:
            node = node.left
        return node.value

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        node = self.root
        if self.empty():
            return None
        while node.right.value != None:
            node = node.right
        return node.value

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
            node = node.getSuccessor
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
        return None

    """permute the info values of the list 

    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    """

    def permutation(self):
        return None

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
        return None

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """



    def getRoot(self):
        return self.root

    def fixSize(self,node):
        tmp_node = node
        while (tmp_node != None):
            tmp_node.size += 1
            tmp_node = tmp_node.parent

    def fix_and_rotate_right(self, node):
        self.updateParentsHeight(node)
        self.fixSize(node)
        tmp_node = node
        cnt = 0
        while (tmp_node.getBalanceFactor() != 1 or tmp_node.getBalanceFactor() != -1):
            if tmp_node.getBalanceFactor() == 0:
                break
            if tmp_node.getBalanceFactor() == -2:
                tmp_node.left_rotation()
                cnt +=1
                break
            if tmp_node.getBalanceFactor() == 2:
                tmp_node.left.left_rotation()
                tmp_node.right_rotation()
                cnt += 2
                break
            tmp_node = tmp_node.parent
        self.updateParentsHeight()
        return cnt


    def fix_and_rotate_left(self, node):
        self.updateParentsHeight(node)
        self.fixSize(node)
        tmp_node = node
        cnt = 0
        while (tmp_node.getBalanceFactor != 1 or tmp_node.getBalanceFactor != -1):
            if tmp_node.getBalanceFactor == 0:
                break
            if tmp_node.getBalanceFactor == 2:
                tmp_node.right_rotation()
                cnt += 1
                break
            if tmp_node.getBalanceFactor == -2:
                tmp_node.right.right_rotation()
                tmp_node.left_rotation()
                cnt += 2
                break
            tmp_node = tmp_node.parent
        self.updateParentsHeight()
        return cnt


    # Using variables the same way as the lecture presentation. B has BF of +2 and A is its left child.
    def right_rotation(self,node):  # Maintaining size attributes
        B = node
        A = node.left
        Size_B = B.size
        C = B.parent
        BOOL = False  # if bool == True then B is the left child of its parent, else it is the right child
        if (C.left == B):
            BOOL = True
        B.left = A.right
        B.left.parent = B
        A.right = B
        A.parent = B.parent
        if BOOL == True:
            A.parent.left = A
        else:  # Bool is false
            A.parent.right = A
        B.parent = A
        A.size = Size_B
        B.size = B.left.size + B.right.size + 1

    def left_rotation(self,node):
        B = node
        A = node.right
        Size_B = B.size
        C = B.parent
        BOOL = False  # if bool == True then B is the right child of its parent, else it is the left child
        if C.right == B:
            BOOL = True
        B.right = A.left
        B.right.parent = B
        A.left = B
        A.parent = B.parent
        if BOOL == True:
            A.parent.right = A
        else:  # Bool is false
            A.parent.left = A
        B.parent = A
        A.size = Size_B
        B.size = B.left.size + B.right.size + 1

    def updateParentsHeight(self,node):
        node1 = node
        while (node1 != None):
            tmp_Height = node1.setRealHeight()
            if node1.height == tmp_Height:
                break
            node1.height = tmp_Height
            node1.balanceFactor = node1.getBalanceFactor()
            node1 = node1.parent
