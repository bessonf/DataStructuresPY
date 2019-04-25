class LinkedList: 
	
	# initialize head and size
	def __init__(self, size=0):
		self.head = self._Node_(None)
		self.size = size
		self.iteration = 0
		#for i in range(0, size):
			#self.add(1)
	
	# --------------- Private ---------------

	# class for node of type
	class _Node_:

		# Creates a new node with a null next field
		def __init__(self, dataItem=None, nodeRef=None):
			self.data	= dataItem;		# store data item
			self.after	= nodeRef;		# for node only dataItem provided, set next equal to null

	# Get node at specified index
	def _getNode_(self, index):
		node = self.head;  
		#for (int i = 0; i < index && node != null; i++) {
		for i in range(0, index):
			if node != None:
				node = node.after
			else:
				break
		return node		#once i reaches index, return current node
	
	# Get at specified index
	def get(self, index): 
		node = self.head;  
		for i in range(0, index):
			if node != None:
				node = node.after
			else:
				break
		return node.data; #once i reaches index, return current node
	
	# store item at index 0 (in head)
	def _addFirst_(self, item): 
		self.head = self._Node_(item, self.head)
		self.size = self.size + 1	# Increase size by 1 
	
	# remove node at index 0
	def _removeFirst_(self):	
		temp = self.head
		if self.head is not None:
			self.head = self.head.after # redefine head as next node
		if temp is not None:   
			self.size = self.size - 1	# decrease size by 1	
	
	# add node with item after reference node
	def _addAfter_ (self, node, item):
		node.after 	= self._Node_(item, node.after) # make new node at node.next with item stored
		self.size 	= self.size + 1			# increase size by 1
	
	# remove node after reference node
	def _removeAfter_ (self, node):  
		temp = node.after; # set temp equal to node after reference node
		if temp is not None:	
			node.after = temp.after		# if node after reference node not null, set node after ref node equal to temp	 
			self.size = self.size - 1	# decrease size by 1	
	
	# --------------- Public (List Interface & toString) ---------------
	
	# boolean test if linkedList is empty
	def isEmpty(self):
		if self.size == 0:
			return True
		else:
			return False

	# Get size of linked list
	def getSize(self):
		return self.size
	
	# add node with item after last node (index = size)
	def add(self, item, index=None):
		if index is None:
			index = self.size

		# if index outside of accessible indecies, throw err
		if index < 0 or index > self.size:	 
			raise Exception('index should be within bounds 0 - {}'.format(self.size)) 
		
		# if index == 0, add item using _addFirst_
		if index == 0:	 
			self._addFirst_(item) 

		# else, add node after last node
		else:	
			node = self._getNode_(index-1)  
			self._addAfter_(node, item)
	
	# remove node at index
	def remove(self, item=None, index=None):
		if index is not None and item is None:
			# if index outside of accessible indecies, throw err
			if index < 0 or index > self.size:	 
				raise Exception('index should be within bounds 0 - {}'.format(self.size)) 

			# if index == 0, add item using _addFirst_
			if index == 0:	   
				self._removeFirst_()	

			# else, add node after last node
			else:	
				node = self._getNode_(index-1)	
				self._removeAfter_(node) 
		
		elif item is not None and index is None:
			count = 0
			nodeRef = self.head
			while nodeRef is not None:
				if str(nodeRef.data) ==	str(item):
					if count == 0: 
						self._removeFirst_()
					else:
						node = self._getNode_(count-1)   
						self._removeAfter_(node)
				nodeRef = nodeRef.after
				count = count + 1

		else:
			raise Exception('index AND item are specified. \nOnly one may be specified') 

	# return duplicate of Linkedlist
	def duplicate(self):
		
		return_list = LinkedList()
		
		nodeRef = self.head
				
		while nodeRef.after is not None:
			return_list.add(nodeRef.data)
			nodeRef = nodeRef.after

		return return_list
	
	# return reverse duplicate of Linkedlist 
	def duplicateReversed(self):
		
		return_list = LinkedList()
		
		i_node = self.size-1
		nodeRef = self._getNode_(i_node)
				
		while i_node >= 0:
			if nodeRef.after is not None:
				 return_list.add(nodeRef.data)
			i_node = i_node - 1
			nodeRef = self._getNode_(i_node);

		return return_list;	
	
	# return size and contents of LinkedList as a string 
	def toString(self):
		
		nodeRef = self.head; 
		result = "[ size: " + str(self.size) + " "
		
		count = 0;
		if nodeRef.after is not None:
			while nodeRef.after is not None:	  
				if count > 0: 
					result = result + ", "
				if nodeRef.after is not None:
					result = result + str(nodeRef.data)
				nodeRef = nodeRef.after 
				count = count + 1
			result = result + " ]"
		return result
	
	def __next__(self): # Python 3: def __next__(self)
		if self.iteration > self.size - 1:
			raise StopIteration
		else:
			self.iteration += 1
			return self.get(self.iteration - 1)

	def __iter__(self):
		self.iteration = 0
		return self

	def __setitem__(self, index, data):
		self.add(data, index)
		self.remove(index=index+1)

	def __getitem__(self, index):
		return self.get(index)
#def __next__(self): #raise StopIteration when done
