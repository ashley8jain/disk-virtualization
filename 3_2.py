execfile('3_1.py')


import random as rnd

bad_block = []

## replication

def createDiskR(id, size):
	if((size*2)>len(freeBlocks)):
		print "Low space!!!"
	elif id in disk_ID:
		print "given disk_ID is already existed!!"
	else:
		createDisk(id,size)
		createDisk(str(id)+"backup@BACKUP#backup",size)




def readReplic(ID,Block_No):
	if ID not in disk_ID:
		print "given disk_ID doesn't exist"
	elif Block_No<0 or Block_No>len(map_ID_diskData[ID]):
		print "index block_no is out of bound!!"
	else:
		rand = rnd.randint(1,100)
		block_index = map_ID_diskData[ID][Block_No]
		if block_index in bad_block or rand<10:
			print "error occurred from first copy"
			data = readDisk(str(ID)+"backup@BACKUP#backup",Block_No)
			# print "bad_block_index:"
			# print map_ID_diskData[ID][Block_No]
			block_index = map_ID_diskData[ID][Block_No]
			bad_block.append(block_index)
			if not freeBlocks:
				print "can't replicated again due to unavailable free space"
			else:
				map_ID_diskData[ID][Block_No] = freeBlocks[0]
				# print "new_index:"
				# print map_ID_diskData[ID][Block_No]
				freeBlocks.remove(freeBlocks[0])
				writeDisk(ID,Block_No,data)
				# print freeBlocks
				# print bad_block
		else:
			readDisk(ID,Block_No)




def writeReplic(ID,Block_No,Block_info):
	if ID not in disk_ID:
		print "given disk_ID doesn't exist"
	elif Block_No<0 or Block_No>len(map_ID_diskData[ID]):
		print "index block_no is out of bound!!"
	else:
		writeDisk(ID,Block_No,Block_info)
		writeDisk(str(ID)+"backup@BACKUP#backup",Block_No,Block_info)




def DeleteDiskR(ID):
	if ID not in disk_ID:
		print "given disk_ID doesn't exist"
	else:
		DeleteDisk(ID)
		DeleteDisk(str(ID)+"backup@BACKUP#backup")


##testing
# createDiskR(12,50)
# createDiskR(13,50)
# createDiskR(14,50)

# writeReplic(12,6,"vrsd")
# readReplic(12,6)

# print len(freeBlocks)

# createDiskR(15,50)
# createDiskR(16,50)


# writeReplic(12,5,"frefe")
# readReplic(12,5)