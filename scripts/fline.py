import ape
from ape.exceptions import ContractLogicError
from rich import print


def main():
    account = ape.accounts.test_accounts[0]
    registry = ape.project.Registry.deploy(sender=account)
    contract = ape.project.VyperContract.deploy(registry, sender=account)

    # Trace should automatically show since it's uncaught
    txn = contract.addBalance_f.as_transaction(123)

    try:
        account.call(txn)
    except ContractLogicError:
        pass

    receipt = txn.provider.get_receipt(txn.txn_hash.hex())
    receipt.show_source_traceback()
