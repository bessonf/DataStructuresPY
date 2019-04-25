
from LinkedList import LinkedList
from HashTableChain import HashTableChain
'''
HashT = HashTableChain();

add_list = ['kevin', 'Frank', 'Micahel', 'Steven', 'Kelsey', 'KeLSey', 'yeet', 'ficl', 'candle']

for word in add_list:
	HashT.add(word.lower(), word)

print(HashT.toString())
'''

# Linked List test
LList = LinkedList()
LList.add('Frank')
LList.add(None)
LList.add('Michael')
LList.add('Steven')


print("\nIsEmpty: ", LList.isEmpty())
print("Size: ", LList.getSize())
print(LList.toString())



'''
for name in LList:
	print("Name: ", name)

print()

TList = LList.duplicateReversed()
for name in TList:
	print("Name: ", name)
'''
