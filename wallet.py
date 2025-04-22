import uuid

class Wallet:
    def __init__(self):
        self.address = self.generate_address()

    def generate_address(self):
        return str(uuid.uuid4())
