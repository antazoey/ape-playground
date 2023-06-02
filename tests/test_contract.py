import ape
from ape_vyper.exceptions import NonPayableError, FallbackNotDefinedError


# When only this test runs, you get 3/5 lines covered.
# This is because it hits the non-payable check (and passes)
# and then runs the 2 source code lines.
def test_happy_path(contract, account):
    receipt = contract.foo_method(5, sender=account)
    assert receipt.return_value is True


# This won't increase statement coverage but would increase branch cov
# (once we add it)
def test_sad_path(contract, account):
    with ape.reverts(dev_message="dev: sub-zero"):
        contract.foo_method(0, sender=account)


# This also won't increase statement cov because the check is covered
# in the happy path. However, it would increase branch cov (once added).
def test_non_payable(contract, account):
    with ape.reverts(NonPayableError):
        contract.foo_method(5, sender=account, value=1)


# Needed for full coverage to ensure the contract reverts on __default__
# since no __default__ was provided and that is the default.
def test_no_default_method(contract, account):
    with ape.reverts(FallbackNotDefinedError):
        contract(sender=account)
