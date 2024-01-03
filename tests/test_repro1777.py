def test_deny(owner, contract, scammer):
    contract.deny(scammer, sender=owner)
    assert contract.checkAccess(scammer) is True
