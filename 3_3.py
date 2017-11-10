execfile('3_1.py')

snapshots = dict()

def Checkpoint(ID,No):
	#TODO
	if (ID not in snapshots):
		snapshots[ID] = {}
		content_ar = []
		for c in map_ID_diskData[ID]:
			content_ar.append(readDisk(ID, c))
		snapshots[ID][No] = content_ar
	else:
		if (No in snapshots[ID]):
			print "Checkpoint_No already exists, please enter new number."
		else:
			content_ar = []
			for c in map_ID_diskData[ID]:
				content_ar.append(readDisk(ID, c))			
			snapshots[ID][No] = content_ar


def Rollback(ID,Checkpoint_No):
	#TODO
	if (ID in snapshots):
		if (Checkpoint_No in snapshots[ID]):
			for block_no in xrange(len(snapshots[ID][Checkpoint_No])):
				writeDisk(ID, block_no, snapshots[ID][Checkpoint_No][block_no])
		else:
			print "No such Checkpoint, enter correct Checkpoint_No"
	else:
		print "No snapshot has created for this ID"


# testing

# createDisk("12",100)
# writeDisk("12",10,"Hello")
# print readDisk("12",10)

# Checkpoint("12",1)


# writeDisk("12",10,"Bipul")
# print readDisk("12",10)

# Checkpoint("12",2)


# Rollback("12",1)
# print readDisk("12",10)

# Rollback("12",2)
# print readDisk("12",10)
