import ape


def main():
    account = ape.accounts.test_accounts[0]
    contract = account.deploy(ape.project.VyperMathDevChecks)
    contract.num_add(1, sender=account)
