def test_fails(contract, account):
    assert 3 == 3
    assert len([]) == 0
    
    receipt = contract.addBalance(123, sender=account)
    assert not receipt.failed

    receipt = contract.addBalance_f(123, sender=account)
    assert not receipt.failed
