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
        self.height = -1
        self.setSize(self)
        self.RealHeight = 0

    def addSize(self):
        tmp_node = self
        while (tmp_node != None):
            tmp_node.size += 1
            tmp_node = tmp_node.parent

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
        node = self
        if node.value == None:
            return -1
        return max(node.left, node.right) + 1

    """sets left child

	@type node: AVLNode
	@param node: a node
	"""

    def setLeft(self, node):
        node.parent = self
        self.left = node
        node.addSize()
        self.updateAll_RealHeight()
        self.fix_and_rotate_left()

    """sets right child

	@type node: AVLNode
	@param node: a node
	"""

    def setRight(self, node):
        node.parent = self
        self.right = node
        node.addSize()
        self.updateAll_RealHeight()
        self.fix_and_rotate_right()

    def fix_and_rotate_right(self):
        tmp_node = self
        while (tmp_node.height != 1 or tmp_node.height != -1):
            if tmp_node.height == 0:
                break
            if tmp_node.height == -2:
                tmp_node.left_rotation()
                break
            if tmp_node.height == 2:
                tmp_node.left.left_rotation()
                tmp_node.right_rotation()
                break
            tmp_node = tmp_node.parent
        self.updateAll_RealHeight()

    def fix_and_rotate_left(self):
        tmp_node = self
        while (tmp_node.height != 1 or tmp_node.height != -1):
            if tmp_node.height == 0:
                break
            if tmp_node.height == 2:
                tmp_node.right_rotation()
                break
            if tmp_node.height == -2:
                tmp_node.right.right_rotation()
                tmp_node.left_rotation()
                break
            tmp_node = tmp_node.parent

    # Using variables the same way as the lecturee presentation. B has BF of +2 and A is its left child.
    def right_rotation(self):  # Maintaining size attributes
        B = self
        A = self.left
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

    def left_rotation(self):
        B = self
        A = self.right
        Size_B = B.size
        C = B.parent
        BOOL = False  # if bool == True then B is the right child of its parent, else it is the left child
        if (C.right == B):
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

    # Updating the height of a node
    def setRealHeight(self):
        if (self.right.value == None):
            self.RealHeight = self.left.RealHeight + 1
            return self.RealHeight
        if (self.left.value == None):
            self.RealHeight = self.right.RealHeight + 1
            return self.RealHeight
        else:
            self.RealHeight = 1 + max(self.left.RealHeight, self.right.RealHeight)
            return self.RealHeight

    def updateAll_RealHeight(self):
        node1 = self
        while (node1 != None):
            tmp_realHeight = node1.setRealHeight()
            if node1.RealHeight == tmp_realHeight:
                break
            node1.RealHeight = tmp_realHeight
            node1.height = node1.getBalanceFactor()
            node1 = node1.parent

    def getBalanceFactor(self):
        return (self.left.RealHeight - self.right.RealHeight)

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

    """returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

    # O(1)
    def isRealNode(self):
        if self.value == None:
            return False
        return True


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
	Constructor, you are allowed to add more fields.  

	"""

    def __init__(self):
        self.root = None

    # add your fields here

    ###	Yuval added from here
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
    	return self.root == None

    """retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""

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
        return -1

    """deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def delete(self, i):
        return -1

    """returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""

    def first(self):
        return None

    """returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""

    def last(self):
        return None

    """returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""

    def listToArray(self):
        return None

    """returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""

    def length(self):
        return None

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
        return None

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
        return None
