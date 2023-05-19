import ape
import click
from ape.cli import NetworkBoundCommand, network_option


_TESTS = ("pay", "pay2", "empty_revert", "empty_revert2", "both", "both2")


@click.command(cls=NetworkBoundCommand)
@network_option()
@click.option("--test", type=click.Choice(_TESTS), required=True)
def cli(network, test):
    account = ape.accounts.test_accounts[0]
    contract = account.deploy(ape.project.Pay)
    if test == _TESTS[0]:
        # Fail on first method because of nonpayable check
        contract.dontpay(1, sender=account, value=1)
    elif test == _TESTS[1]:
        # Fail on second method because of nonpayable check
        contract.dontpay(1, sender=account, value=1)
    elif test == _TESTS[2]:
        # Fail on first empty revert to see how it compares
        contract.dontpay(0, sender=account)
    elif test == _TESTS[3]:
        # Fail on first empty revert to see how it compares
        contract.dontpay2(0, sender=account)
    elif test == _TESTS[4]:
        # Use both value and cause empty revert fail.
        # Hopefully value check fails first...
        contract.dontpay(0, sender=account, value=1)
    elif test == _TESTS[5]:
        # Use both value and cause empty revert fail.
        # Hopefully value check fails first...
        contract.dontpay2(0, sender=account, value=1)
