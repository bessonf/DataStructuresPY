from LinkedList import LinkedList

class HashTableChain:
	
	numKeys = 0				# The number of keys in HashTableChain

	#	Constructor for when no size is provided
	def __init__(self, CAPACITY=11, LOAD_THRESHOLD=.75):
			self.CAPACITY 		= CAPACITY
			self.LOAD_THRESHOLD = LOAD_THRESHOLD
			self.numKeys 		= 0
			self.table 			= LinkedList(CAPACITY)

	#	Entry class that holds key:value pair 
	class Entry:

		# Entry constructor class 
		def __init__(self, key, value):
			self.key = key
			self.value = value
		
		# Get key from entry
		def getKey(self):
			return self.key

		# Get val from entry 
		def getValue(self):
			return self.value

		# Set val in entry 
		def setValue(self, val):
			oldVal = self.value
			self.value = val
			return oldVal
		
		# Return string of key:val pair */
		def toString(self):
			return str(self.key) + " = " + str(self.value)

	# Get value at a specified key 
	def get(self, key):
		index = hash(key) % self.table.getSize()
		
		if index < 0:
			index += self.table.getSize()
	
		if self.table[index] is None:
			return None # key is not in the table.

		# Search the list at table[index] to find the key.
		for nextItem in self.table[index]:
			if nextItem == key: 
				return nextItem.value

		return None
 
	# Add key:val pair to HashTableChain
	def add(self, key, value):
		index = hash(key) % self.table.getSize()
		
		if index < 0:
			index += self.table.getSize()

		if self.table[index] is None:
			self.table[index] = LinkedList()	  # Create a new linked list at table[index].
	
		# Search the list at table[index] to find the key.
		found_val = False
		for nextItem in self.table[index]:
			if nextItem.value == value: 
				found_val = True
		
		if not found_val:
			self.table[index].add(self.Entry(key, value))
			self.numKeys += 1
		
		print(self.numKeys, self.LOAD_THRESHOLD * self.table.getSize())
		if self.numKeys > (self.LOAD_THRESHOLD * self.table.getSize()):
			
			self.rehash()
		
		return None
	
	# Check if HashTable chain is empty 
	def isEmpty(self):
		return self.numKeys == 0
	
	# Double size + 1 of HashTableChain and reinsert key:val pairs
	def rehash(self):
		oldTable 	 = self.table
		self.table 	 = LinkedList(oldTable.getSize() * 2 + 1)
		self.numKeys = 0
		for singleLinkedList in oldTable:
			if singleLinkedList is not None:
				for entry in singleLinkedList:
					self.add(entry.getKey(), entry.getValue())

	# Check if HashTableChain contains key:val pair
	def contains(self, key, value):
		index = hash(key) % self.table.getSize()
		
		if index < 0:
			index += self.table.getSize()

		if self.table[index] is None:
			return False # key is not in table

		for entry in self.table[index]:
			if entry.getValue() == value:
				return True
		
		return False
	
	# Remove key:val pair from HashTableChain 
	def remove(self, key, value):
		index = hash(key) % self.table.getSize()
		
		if index < 0:
			index += self.table.getSize()
		
		if self.table[index] is None:
			return False # key is not in table

		for entry in self.table[index]:
			if entry.getValue() == value:
				self.table[index].remove(entry)
				self.numKeys -= 1
				if self.table[index].isEmpty():
					self.table[index] = None
				return True
			
		return False

	# Return size of HashTableChain
	def size(self):
		return self.numKeys
	
	# Get a preview (row 0-2) of HashTableChain
	def toString(self):
		#for (int i = 0; i < table.length; i++) {
		sb = ""
		for i in range(0, self.table.getSize()):
			sb = sb + "row:" + str(i) + "\t"
			if self.table[i] is not None:
				for entry in self.table[i]:
					sb = sb + "-> " + entry.toString() + " "
			else:
			  sb = sb + "None"	
			sb = sb + "\n"
		return sb
	
	'''
	Generate near misses for a given string 
	[x] Construct every string that can be made by deleting one letter from the word. (n possibilities, where n is the length of the word)
	[x] Construct every string that can be made by inserting any letter of the alphabet at any position in the string. (26*(n+1) possibilities)
	[x] Construct every string that can be made by swapping two neighboring characters in the string. (n-1 possibilities)
	[x] Construct every string that can be made by replacing each letter in the word with some letter of the alphabet. (26*n possibilities (including the original word n times, which is probably easier than avoiding it))
	[x] Construct every pair of strings that can be made by inserting a space into the word. (n-1 pairs of words; you have to check separately in the dictionary for each word in the pair)
	'''
	def generateNearMisses(searchInput):
		NearMisses = []
		i_tot = 0 

		# Delete single char (n possibilities)
		for i in range(0, len(searchInput)):
			buildStr = searchInput[:i] + searchInput[(i+1):] # deleteCharAt(i)
			NearMisses.append(buildStr)
			i_tot = i_tot + 1

		# insert any letter of the alphabet (26*(n+1) possibilities)
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		for i in range(0, len(searchInput)):
			for i_let in range(0, len(alphabet)):
				buildStr = searchInput[:i] + alphabet[i_let] + searchInput[i] + searchInput[(i+1):]		# insert(i, alphabet[i_let]);
				NearMisses.append(buildStr)
				i_tot = i_tot + 1

		# Swap two char (n-1 possibilities)
		for i in range(0, len(searchInput)-1):
			if searchInput[i] != searchInput[i+1]:
				buildStr = searchInput[:i] + searchInput[i+1] + searchInput[i] + searchInput[(i+2):]
				NearMisses.append(buildStr)
				i_tot = i_tot + 1

		# Replace char with any letter of the alphabet (26*n possibilites)
		for i in range(0, len(searchInput)):
			for i_let in range(0, len(alphabet)):
				#if (buildStr.charAt(i) != alphabet[i_let]) {
				buildStr = searchInput[:i] + alphabet[i_let] + searchInput[(i+1):] 
				NearMisses.append(buildStr)
				i_tot = i_tot + 1

		# insert a space (n-1 pairs, 2*(n-1) words)
		for i in range(1, len(searchInput)):
			buildStr = []
			buildStr.append(searchInput[:i])
			buildStr.append(searchInput[i:])
			for string in buildStr:
				if string != "":
					NearMisses.append(string)
					i_tot = i_tot + 1

		'''
		// Caps
		for (int i = 0; i < str.length(); i++) {
			StringBuilder buildStr = new StringBuilder(str);
			char testChar = str.charAt(i);
			if (Character.isUpperCase(testChar)){
				testChar = Character.toLowerCase(testChar);
			} else if (Character.isLowerCase(testChar)) {
				testChar = Character.toUpperCase(testChar);
			} else {
				continue;
			}
			buildStr.setCharAt(i, testChar);
			 NearMisses.add(buildStr.toString());
			i_tot = i_tot + 1;
		}
		'''
		
	   # return NearMisses.sort()						#with repeats
		return list(dict.fromkeys(NearMisses)).sort()	#without repeats