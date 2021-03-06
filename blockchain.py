import hashlib
import json
from time import time

class Blockchain(object):
    """
    Blockchain class:
        functions:
            __init__
            new_block
            new_transaction
            hash
            last_block
        Block Example:
        {
            'index': 1,
            'timestamp': 1506057125.900785,
            'transactions': [
                {
                    'sender': "8527147fe1f5426f9dd545de4b27ee00",
                    'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
                    'amount': 5,
                }
            ],
            'proof': 324984774000,
            'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
        }
    """
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Genesis
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[:-1]
