def test_contract(contract, account):
    receipt = contract.register(5, sender=account)
    assert not receipt.failed
