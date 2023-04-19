import ape


def main():
    account = ape.accounts.test_accounts[0]
    contract = account.deploy(ape.project.VyperMathDevChecks)
    contract.num_add(0, sender=account, value=1)
