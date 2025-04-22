from block import Block
from transaction import Transaction

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = 2
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def proof_of_work(self, block):
        block.nonce = 0
        while not block.hash.startswith("0" * self.difficulty):
            block.nonce += 1
            block.hash = block.compute_hash()
        return block

    def mine(self):
        if not self.pending_transactions:
            return False

        last_block = self.get_last_block()
        new_block = Block(index=last_block.index + 1,
                          transactions=[t.to_dict() for t in self.pending_transactions],
                          previous_hash=last_block.hash)
        
        proofed_block = self.proof_of_work(new_block)
        self.chain.append(proofed_block)
        self.pending_transactions = []
        return proofed_block
