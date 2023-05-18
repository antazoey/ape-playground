def test_antazoey(contract, account):
    receipt = contract.antazoey(5, sender=account)
    assert receipt.return_value is True
