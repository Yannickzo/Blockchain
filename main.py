import hashlib

from numpy import block
class YannickCoinBlock:
    def __init__(self , previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{'- '.join(transaction_list)} - {previous_block_hash}"
        self.previous_block_hash = hashlib.sha256(self.block_data.encode()).hexdigest
# YC refers to YannickCoin
t1 = "Mark sends 5 YC to Noah"
t2 = "Noah sends 4.5 YC to james"
t3 = "james sends 6.8 YC to Yannick"
t4 = "Yannick sends 3.9 YC to Allison"

block1 = YannickCoinBlock('firstblock', [t1 , t2])
print(f"Block 1 data : {block1.block_data}")
print(f"Block 1 hash : {block1.previous_block_hash}")

block2 = YannickCoinBlock(block1.previous_block_hash, [t3 , t4])
print(f"Block 2 data : {block2.block_data}")
print(f"Block 2 hash : {block2.previous_block_hash}")