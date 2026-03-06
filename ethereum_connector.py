from web3 import Web3
import json

# Hardhat local blockchain
GANACHE_URL = "http://127.0.0.1:8545"

# Contract address from deployment
CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

# ABI file
ABI_PATH = "json/VaccineSupplyChain_compData.json"


def connect_web3():
    w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

    if not w3.is_connected():
        raise Exception("Blockchain node not connected")

    return w3


def load_contract():
    w3 = connect_web3()

    with open(ABI_PATH, "r") as f:
        contract_json = json.load(f)

    contract = w3.eth.contract(
        address=CONTRACT_ADDRESS,
        abi=contract_json["abi"]
    )

    return w3, contract


# ---------------------------
# REGISTER BATCH
# ---------------------------
def register_batch(batch_id, vaccine_name, manufacturer):

    w3, contract = load_contract()
    account = w3.eth.accounts[0]

    tx_hash = contract.functions.registerBatch(
        batch_id,
        vaccine_name,
        manufacturer
    ).transact({
        "from": account
    })

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    return {
        "status": "success",
        "tx_hash": receipt.transactionHash.hex()
    }


# ---------------------------
# TRANSFER BATCH
# ---------------------------
def transfer_batch(batch_id, new_holder):

    w3, contract = load_contract()
    account = w3.eth.accounts[0]

    tx_hash = contract.functions.transferBatch(
        batch_id,
        new_holder
    ).transact({
        "from": account
    })

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    return {
        "status": "success",
        "tx_hash": receipt.transactionHash.hex()
    }


# ---------------------------
# GET BATCH DETAILS
# ---------------------------
def get_batch(batch_id):

    w3, contract = load_contract()

    batch = contract.functions.getBatch(batch_id).call()

    return {
        "batchId": batch[0],
        "vaccineName": batch[1],
        "manufacturer": batch[2],
        "currentHolder": batch[3]
    }