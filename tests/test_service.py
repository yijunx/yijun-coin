import app.services.blockchain as BlockChainService
from app.models.blockchain import Blockchain

BLOCKCHAIN = Blockchain(
    **{
        "difficulty": 4,
        "chain": [
            {
                "nonce": 5670,
                "previous_hash": "0000000000000000000000000000000000000000000000000000000000000000",
                "data": "hello",
                "number": 0,
            },
            {
                "nonce": 36697,
                "previous_hash": "0000407992cf0f808d13ff4b4d6dabc475c5d812c9f6b4dac175d9c0ed2d98dc",
                "data": "whats up",
                "number": 1,
            },
            {
                "nonce": 33046,
                "previous_hash": "00002b1d6482e9275d72b5d7c95dbafada307a8232cdc533f0cb932956c653e1",
                "data": "good bye",
                "number": 2,
            },
            {
                "nonce": 13859,
                "previous_hash": "0000f9e1f72662e5c593e8878ac7f49b6c983d4ec97d223e886435fd5690c47f",
                "data": "yoyo",
                "number": 3,
            },
        ],
    }
)


def test_sync_chain():
    BlockChainService.sync_blockchain(blockchain=BLOCKCHAIN)


def test_get_chain():
    blockchain = BlockChainService.get_blockchain()
    assert blockchain.chain[3].nonce == BLOCKCHAIN.chain[3].nonce
    assert blockchain.isValid()
