import ape


def main():
    account = ape.accounts.test_accounts[0]
    registry = ape.project.Registry.deploy(sender=account)
    contract = ape.project.VyperContract.deploy(registry, sender=account)
    receipt = contract.addBalance(contract._balance(), sender=account)
