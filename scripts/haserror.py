import ape


def main():
    account = ape.accounts.test_accounts[0]
    other = ape.accounts.test_accounts[1]
    contract = ape.project.HasError.deploy(sender=account)
    contract.withdraw(sender=other)
