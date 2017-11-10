A = [bytearray(100)] * 200
B = [bytearray(100)] * 300

freeBlocks = range(0,500)
disk_ID = []
map_ID_diskData = dict()


## consolidation

#read data
def read(block_No):
	if block_No < 200:
		data = A[block_No]
		# print data
		return data
	else:
		data2 = B[block_No-200]
		# print data2
		return data2

#write data into disk
def write(block_No,block_inf):
	if block_No < 500:
		if block_No < 200:
			A[block_No]=block_inf
		else:
			B[block_No-200]=block_inf
	else:
		print "index block_no is out of bound!!"


## testing for read n write API
# write(100,"Hello")
# print read(100)






## partitioning

def createDisk(id, size):
	global freeBlocks
	if(size>len(freeBlocks)):
		print "Low space!!!"
	elif id in disk_ID:
		print "given disk_ID is already existed!!"
	else:
		disk_ID.append(id)
		diskData = freeBlocks[0:size]
		map_ID_diskData[id]=diskData
		freeBlocks = freeBlocks[size:]

def readDisk(ID,Block_No):
	if ID not in disk_ID:
		print "given disk_ID doesn't exist"
	elif Block_No<0 or Block_No>len(map_ID_diskData[ID]):
		print "index block_no is out of bound!!"
	else:
		return read(map_ID_diskData[ID][Block_No])

def writeDisk(ID,Block_No,Block_info):
	if ID not in disk_ID:
		print "given disk_ID doesn't exist"
	elif Block_No<0 or Block_No>len(map_ID_diskData[ID]):
		print "index block_no is out of bound!!"
	else:
		write(map_ID_diskData[ID][Block_No],Block_info)

def DeleteDisk(ID):
	global freeBlocks
	if ID not in disk_ID:
		print "given disk_ID doesn't exist"
	else:
		freeBlocks = freeBlocks+map_ID_diskData[ID]
		del map_ID_diskData[ID]
		disk_ID.remove(ID)



## testing

# createDisk("12",100)
# writeDisk("12",10,"Hello")
# readDisk("12",10)

# createDisk("123",100)
# writeDisk("123",10,"Hello2")
# readDisk("123",10)

# createDisk("12",100)

# DeleteDisk("123")
# readDisk("123",10)