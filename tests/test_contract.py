import pytest
import ape


# def test_fails(contract, account):
#     assert 3 == 3
#     assert len([]) == 0

#     receipt = contract.addBalance(123, sender=account)
#     assert not receipt.failed

#     receipt = contract.addBalance_f(123, sender=account)
#     assert not receipt.failed


def test_success(contract, account):
    contract.addBalance(123, sender=account)


# def test_add_zero(contract, account):
#     with ape.reverts():
#         contract.addBalance_f(0, sender=account)


@pytest.mark.use_network("ethereum:local:test")
def test_a(chain):
    assert chain.provider.name == "test"

def test_register_already_registered(contract, account):
    with ape.reverts(dev_message="dev: yo dont"):
        contract.addBalance_f(123, sender=account)

@pytest.mark.use_network("ethereum:local:test")
def test_b(chain):
    assert chain.provider.name == "test"
