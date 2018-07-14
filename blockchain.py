from block import Block
import datetime

b1 = Block.create_genesis_block()
print(b1.hash)

block_chain = [Block.create_genesis_block()]

num_blocks_to_add = input("Enter the number of blocks to be added:")

for i in range(1, num_blocks_to_add+1):
	data = raw_input("Enter the data to be entered:")
	block_chain.append(Block(block_chain[-1].hash, data, datetime.datetime.now()))
	print("Block #%d has been created." %i)
	print("Block #%d hash: %s"%(i, block_chain[i].hash))
	print("")