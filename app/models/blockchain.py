from hashlib import sha256

from pydantic import BaseModel


def update_hash(*args):
    hashing_text = ""
    h = sha256()

    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode("utf-8"))
    return h.hexdigest()


class Block(BaseModel):
    # initial value..
    nonce: int = 0
    previous_hash: str = "0" * 64
    data: str
    number: int = 0

    # def __init__(self, data, number: int = 0) -> None:
    #     self.data = data
    #     self.number = number

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

    def __eq__(self, __value: "Block") -> bool:
        return self.hash() == __value.hash()

    class Config:
        orm_mode = True


class Blockchain(BaseModel):
    difficulty: int = 4
    chain: list[Block] = []

    # def __init__(self, chain: list[Block] = None) -> None:
    #     if chain:
    #         self.chain = chain
    #     else:
    #         self.chain = []

    def add(self, block: Block):
        self.chain.append(block)

    def remove(self, block: Block):
        self.chain.remove(block)

    def mine(self, block: Block):
        try:
            block.previous_hash = self.chain[-1].hash()
        except IndexError:
            pass  # there is previous hash as 64 zeros already

        while True:
            if block.hash()[: self.difficulty] == "0" * self.difficulty:
                self.add(block=block)
                break
            else:
                block.nonce += 1

    def isValid(self) -> bool:
        for previous_block_index, block in enumerate(self.chain[1:]):
            current_blocks_previous_hash = block.previous_hash
            previous_blocks_current_hash = self.chain[previous_block_index].hash()
            if previous_blocks_current_hash[: self.difficulty] != "0" * self.difficulty:
                return False
            if current_blocks_previous_hash != previous_blocks_current_hash:
                return False
        return True


def main():
    blockchain = Blockchain()
    database = ["hello", "whats up", "good bye", "yoyo"]

    for i, data in enumerate(database):
        blockchain.mine(Block(data=data, number=i))

    print(blockchain.dict())

    # corrupt it
    # blockchain.chain[2].data = "newdata"  # makes it not valid
    # blockchain.chain[3].data = "newdata" # last block wont work..
    print(blockchain.isValid())


if __name__ == "__main__":
    main()
