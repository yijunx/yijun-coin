from hashlib import sha256


def update_hash(*args):
    hashing_text = ""
    h = sha256()

    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode("utf-8"))
    return h.hexdigest()


class Block:
    data = None
    # data is like a gives b 5 dollars

    hash = None
    nonce = 0
    # used for proof of work

    previous_hash = "0" * 64
    # 64 is the length of the sha256

    def __init__(self, data, number=0) -> None:
        self.data = data
        self.number = number

    def hash(self):
        return update_hash(self.previous_hash, self.number, self.data, self.nonce)

    def __repr__(self) -> str:
        return f"""
        Block #: {self.number}
        Hash: {self.hash()}
        Previous: {self.previous_hash}
        Data: {self.data}
        Nonce: {self.nonce}
"""


class Blockchain:
    difficulty = 4

    def __init__(self, chain: list[Block] = None) -> None:
        if chain:
            self.chain = chain
        else:
            self.chain = []

    def add(self, block: Block):
        # why not just use the block??
        self.chain.append(
            # {
            #     "hash": block.hash(),
            #     "previous_hash": block.previous_hash,
            #     "number": block.number,
            #     "data": block.data,
            #     "nonce": block.nonce,
            # }
            block
        )

    def mine(self, block: Block):
        try:
            block.previous_hash = self.chain[-1].hash()  # .get("hash")
        except IndexError:
            pass  # there is previous hash as 64 zeros already

        while True:
            if block.hash()[: self.difficulty] == "0" * self.difficulty:
                self.add(block=block)
                break
            else:
                block.nonce += 1


def main():
    blockchain = Blockchain()
    database = ["hello", "whats up", "good bye", "yoyo"]

    for i, data in enumerate(database):
        blockchain.mine(Block(data=data, number=i))

    for block in blockchain.chain:
        print(block)


if __name__ == "__main__":
    main()
