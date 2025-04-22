from blockchain import Blockchain
from wallet import Wallet
from transaction import Transaction
# Tạo ví cho 2 người
alice = Wallet()
bob = Wallet()

# Tạo blockchain
bankchain = Blockchain()

# Giao dịch: Alice gửi 100 cho Bob
tx1 = Transaction(sender=alice.address, receiver=bob.address, amount=50)
bankchain.add_transaction(tx1)

# Đào block mới để xác nhận giao dịch
mined_block = bankchain.mine()

# In ra kết quả
for block in bankchain.chain:
    print(f"\nBlock {block.index}:")
    print(f"Hash: {block.hash}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Transactions: {block.transactions}")
