class BinaryTree:
	
	# initialize tree (head and size)
	def __init__(self, root=None, leftTree=None, rightTree=None):
		self.root = None
		if root is not None:
			self.root = root
		if leftTree is not None:
			self.root.left = leftTree.root
		if rightTree is not None:
			self.root.right = rightTree.root
		self.string = ''

	# class for Node
	class Node:
		
		def __init__(self, data=None, left=None, right=None):
			self.data	= data
			self.left	= left
			self.right	= right

		def toString(self):
			return str(self.data)
	

	''' isEmpty method.
	@return if BinaryTree is empty, returns true
			else, returns false.
	'''
	def isEmpty(self):
		if self.root is None:
			return True
		else:
			return False
	

	''' Recursive add method.
	post: The item is not in the tree;
		  addReturn is true after item stored in tree
		  addReturn is false if item in tree
	@param localRoot The root of the current subtree
	@param item The item to be added
	@return The modified local root leading to the
			proper node that item will be connected to
	'''
	def _add_(self, localRoot, item):
		if localRoot is None:
			# item is not in the tree — insert it.
			# addReturn = true;
			return self.Node(item)
		elif item == localRoot.data:
			# item is equal to localRoot.data
			# addReturn = false;
			return localRoot
		elif item < localRoot.data:
			# item is less than localRoot.data
			localRoot.left = self._add_(localRoot.left, item)
			return localRoot
		else:
			# item is greater than localRoot.data
			localRoot.right = self._add_(localRoot.right, item)
			return localRoot
	
	def add(self, item):
		self.root = self._add_(self.root, item)
		# return addReturn
	

	''' Recursive delete method.
	post: The item is not in the tree;
		  deleteReturn is equal to the deleted item
		  as it was stored in the tree or null
		  if the item was not found.
	@param localRoot The root of the current subtree
	@param item The item to be deleted
	@return The modified local root that does not contain
			the item
	'''
	def _remove_(self, localRoot, item):
		if localRoot is None:
			# item is not in the tree - can't delete it.
			# deleteReturn = false;
			return localRoot
		
		elif item < localRoot.data:
			# item is less than localRoot.data
			localRoot.left = self._remove_(localRoot.left, item)
			return localRoot
		elif item > localRoot.data:
			# item is greater than localRoot.data
			localRoot.right = self._remove_(localRoot.right, item)
			return localRoot
		
		else:
			# deleteReturn = true;
			if localRoot.left is None and localRoot.right is None:
				localRoot = None
				return localRoot
			elif localRoot.left is None and localRoot.right is not None:
				localRoot = localRoot.right
				return localRoot
			elif localRoot.left is not None and localRoot.right is None:				
				localRoot = localRoot.left
				return localRoot
			elif localRoot.left is not None and localRoot.right is not None:
	
				# method 2 in class reading "Binary Search Trees.pdf (smallest element in right subtree)
				if localRoot.right.left is None and localRoot.right.right is None:
					localRoot.data = localRoot.right.data
					localRoot.right = None
				elif localRoot.right.left is None and localRoot.right.right is not None:
					localRoot = localRoot.right
				elif localRoot.right.left is not None:
					tmp_node = localRoot.right
					while tmp_node.left.left is not None: 
						tmp_node	= tmp_node.left
					localRoot.data	= tmp_node.left.data
					tmp_node.left	= None
				return localRoot
			
			else:
				return localRoot
	
	def remove(self, target):
	  self.root = self._remove_(self.root, target)
	  #return deleteReturn
	

	''' Starter method contains.
	 * pre: The target object must implement
	 *		the comparable interface (compareTo).
	 * @param target The Comparable object being sought			 
	 * @return The object, if found, otherwise null
	'''	   
	def _contains_(self, localRoot, target):
		if localRoot is None: 
			return None
		if target == localRoot.data:
			return localRoot.data
		elif target < localRoot.data: 
			return self._contains_(localRoot.left, target)
		else:
			return self._contains_(localRoot.right, target)
	
	def contains(self, target):
		if self._contains_(self.root, target) is None: 
			return False 
		else:
			return True


	''' preOrderTraverse method
	 * @param node The node to be added to order	 
	''' 
	def preOrderTraverse(self, node):
		if node is None:
			pass 
		else:
			self.string = self.string + node.toString() + ', '
			self.preOrderTraverse(node.left)
			self.preOrderTraverse(node.right)
	
	
	''' toString method
	 * @return string containing preOrderTraverse set of data in all nodes
	'''	   
	def toString(self):
		  self.string = ''
		  #preOrderTraverse(root, 1, sb);
		  #return sb.toString();
		  self.preOrderTraverse(self.root)
		  return self.string[:-2]
	
	
