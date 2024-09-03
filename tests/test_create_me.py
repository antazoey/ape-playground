"""
Testing the `CreateMe.vy` contract,
which is only deployed via factory contract
`Factory.vy` in attempts to reproduce or
debug https://github.com/ApeWorX/ape/issues/2262
"""

import ape


def test_assert_not_zero(target_a, antazoey):
    with ape.reverts():
        target_a.assertNotZero(0, sender=antazoey)


def test_assert_purposely_dont_use_targets():
    # Just trying to show an in-between test, in case that matters
    assert True


def test_assert_not_one(target_b, antazoey):
    with ape.reverts():
        target_b.assertNotOne(1, sender=antazoey)
