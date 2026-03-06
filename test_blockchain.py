from blockchain import Blockchain

bc = Blockchain()

bc.add_block("Manufacturer: Batch001 created")
bc.add_block("Distributor: Batch001 shipped")
bc.add_block("Hospital: Batch001 received")

for block in bc.chain:
    print("Index:", block.index)
    print("Data:", block.data)
    print("Hash:", block.hash)
    print("------------------")

print("Is Blockchain Valid?", bc.is_chain_valid())