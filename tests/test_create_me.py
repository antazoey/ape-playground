"""
Testing the `CreateMe.vy` contract,
which is only deployed via factory contract
`Factory.vy` in attempts to reproduce or
debug https://github.com/ApeWorX/ape/issues/2262
"""
import ape

def test_assert_not_zero_is_zero(create_me_contract, antazoey):
    with ape.reverts():
        create_me_contract.assertNotZero(0, sender=antazoey)


def test_assert_not_zero_not_zero(create_me_contract, antazoey):
    tx = create_me_contract.assertNotZero(1, sender=antazoey)
    assert not tx.failed
