import ape
from ape.exceptions import ContractLogicError
from rich import print


def main():
    account = ape.accounts.test_accounts[0]
    registry = ape.project.Registry.deploy(sender=account)
    contract = ape.project.TracebackContract.deploy(registry, sender=account)

    # Trace should automatically show since it's uncaught
    receipt = contract.addBalance_f(123, sender=account)
    print(receipt)
    x = 3

    # doing more stuff after fail

    print(receipt.transaction)
