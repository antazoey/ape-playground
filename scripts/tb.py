import ape
from ape.exceptions import ContractLogicError


def main():
    account = ape.accounts.test_accounts[0]
    registry = ape.project.RegistryF.deploy(sender=account)
    contract = ape.project.JustFail.deploy(registry, sender=account)
    txn = contract.addBalance_f.as_transaction(123)

    try:
        account.call(txn)
    except ContractLogicError:
        pass

    receipt = txn.provider.get_receipt(txn.txn_hash.hex())
    receipt.show_source_traceback()
